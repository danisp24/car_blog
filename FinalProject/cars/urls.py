from django.urls import path

from FinalProject.cars.views import CarListView, CarDetailView, MyBookingsView, ManageBookingsView, \
    UpdateBookingStatusView, CarCreateView, TestDriveBookingCreateView, CarCategoryCreateView, EditBookingsView

urlpatterns = [
    path('home/', CarListView.as_view(), name='cars'),
    path('add/', CarCreateView.as_view(), name='add_car'),
    path('categories/add/', CarCategoryCreateView.as_view(), name='add_category'),
    path('details/<int:pk>/', CarDetailView.as_view(), name='car_details'),
    path('create-booking/', TestDriveBookingCreateView.as_view(), name='book_car'),
    path('edit-booking/<int:pk>/', EditBookingsView.as_view(), name='edit_booking'),
    path('my-bookings/', MyBookingsView.as_view(), name='my_bookings'),
    path('manage-bookings/', ManageBookingsView.as_view(), name='manage_bookings'),
    path('update-booking-status/<int:pk>/', UpdateBookingStatusView.as_view(), name='update_booking_status'),

]
