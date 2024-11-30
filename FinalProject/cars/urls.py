from django.urls import path

from FinalProject.cars.views import CarListView, CarDetailView, MyBookingsView, ManageBookingsView, \
    UpdateBookingStatusView, CarCreateView

urlpatterns = [
    path('home/', CarListView.as_view(), name='cars'),
    path('add/', CarCreateView.as_view(), name='add_car'),
    path('details/<int:pk>/', CarDetailView.as_view(), name='car_details'),
    path('my-bookings/', MyBookingsView.as_view(), name='my_bookings'),
    path('manage-bookings/', ManageBookingsView.as_view(), name='manage_bookings'),
    path('update-booking-status/<int:pk>/', UpdateBookingStatusView.as_view(), name='update_booking_status'),

]
