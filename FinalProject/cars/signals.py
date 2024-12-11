from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from FinalProject.cars.models import TestDriveBooking


@receiver(post_save, sender=TestDriveBooking)
def update_car_availability(sender, instance, **kwargs):
    if instance.status == 'Confirmed':

        TestDriveBooking.objects.filter(
            car=instance.car,
            status='Pending'
        ).exclude(id=instance.id).update(status='Cancelled')

        instance.car.available_for_test_drive = False
        instance.car.save()

    elif instance.status in ['Cancelled', 'Pending']:

        confirmed_bookings = TestDriveBooking.objects.filter(
            car=instance.car,
            status='Confirmed'
        )

        if not confirmed_bookings.exists():
            instance.car.available_for_test_drive = True
            instance.car.save()


@receiver(post_delete, sender=TestDriveBooking)
def update_car_availability_on_delete(sender, instance, **kwargs):
    confirmed_bookings = TestDriveBooking.objects.filter(
        car=instance.car,
        status='Confirmed'
    )

    if not confirmed_bookings.exists():
        instance.car.available_for_test_drive = True
        instance.car.save()
