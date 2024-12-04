from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import CarCreateForm, TestDriveBookingForm
from .models import Car, CarCategory, TestDriveBooking


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'
    paginate_by = 3
    ordering = ['brand']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CarCategory.objects.all()
        return context


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        if request.user.is_authenticated:
            TestDriveBooking.objects.create(
                user=request.user,
                car=car,
                date=request.POST['date'],
                time=request.POST['time'],
            )
            return redirect('car_details', pk=car.pk)
        else:
            return redirect('login')


class CarCreateView(PermissionRequiredMixin, CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/add_car.html'
    success_url = reverse_lazy('cars')
    permission_required = 'cars.add_car'

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)


class MyBookingsView(LoginRequiredMixin, ListView):
    model = TestDriveBooking
    template_name = 'cars/my_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return TestDriveBooking.objects.filter(user=self.request.user).order_by('-created_at')


class TestDriveBookingCreateView(LoginRequiredMixin, CreateView):
    model = TestDriveBooking
    form_class = TestDriveBookingForm
    template_name = 'cars/book_car.html'
    success_url = reverse_lazy('my_bookings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.save()
        return redirect('my_bookings')


class ManageBookingsView(PermissionRequiredMixin, ListView):
    model = TestDriveBooking
    permission_required = 'cars.manage_bookings'
    template_name = 'cars/manage_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return TestDriveBooking.objects.all().order_by('-created_at')


class UpdateBookingStatusView(PermissionRequiredMixin, UpdateView):
    model = TestDriveBooking
    fields = ['status']
    template_name = 'cars/update_booking_status.html'
    permission_required = 'cars.manage_bookings'

    def form_valid(self, form):

        booking = form.save(commit=False)

        if booking.status == 'Confirmed':

            existing_confirmed = TestDriveBooking.objects.filter(
                car=booking.car,
                status='Confirmed'
            ).exclude(id=booking.id)

            if existing_confirmed.exists():
                error_message = 'This car already has a confirmed booking.'
                return render(self.request, '400.html', {'error_message': error_message}, status=400)

            TestDriveBooking.objects.filter(
                car=booking.car,
                status='Pending'
            ).exclude(id=booking.id).update(status='Cancelled')

            booking.car.available_for_test_drive = False
            booking.car.save()

        elif booking.status in ['Cancelled', 'Pending']:
            confirmed_bookings = TestDriveBooking.objects.filter(
                car=booking.car,
                status='Confirmed'
            )

            if not confirmed_bookings.exists():
                booking.car.available_for_test_drive = True
                booking.car.save()

        booking.save()

        return redirect('manage_bookings')

    def form_invalid(self, form):
        error_message = 'Invalid data provided!'
        return render(self.request, '400.html', {'error_message': error_message}, status=400)
