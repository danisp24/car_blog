from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

UserModel = get_user_model()


class Car(models.Model):
    brand = models.CharField(max_length=100)
    category = models.ForeignKey('CarCategory', on_delete=models.CASCADE, related_name='cars')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1000)])
    description = models.TextField()
    # image = models.CloudinaryField(upload_to='car_images/', blank=True, null=True) #TODO
    available_for_test_drive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand}"


class CarCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TestDriveBooking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ('manage_bookings', 'Can manage test drive bookings'),
        ]

    def save(self, *args, **kwargs):
        if self.status == 'Confirmed':

            existing_confirmed = TestDriveBooking.objects.filter(
                car=self.car,
                status='Confirmed'
            ).exclude(id=self.id)

            if existing_confirmed.exists():
                raise ValidationError("This car already has a confirmed booking.")

            TestDriveBooking.objects.filter(
                car=self.car,
                status='Pending'
            ).exclude(id=self.id).update(status='Cancelled')

            self.car.available_for_test_drive = False
            self.car.save()

        elif self.status in ['Cancelled', 'Pending']:
            confirmed_bookings = TestDriveBooking.objects.filter(
                car=self.car,
                status='Confirmed'
            )

            if not confirmed_bookings.exists():
                self.car.available_for_test_drive = True
                self.car.save()

        super().save(*args, **kwargs)
