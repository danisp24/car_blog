from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

UserModel = get_user_model()


class CarCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, related_name='cars')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1000)])
    description = models.TextField()
    image_url = models.URLField(null=True, blank=True,
                                default='https://t3.ftcdn.net/jpg/07/31/17/02/360_F_731170296_Xamy0xpnprlowd7SPEIMHZqTWxJGRqHv.jpg')
    available_for_test_drive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand}"


class TestDriveBooking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ('manage_bookings', 'Can manage test drive bookings'),
        ]

    def __str__(self):
        return f"Booking for {self.car.brand} by {self.user.username}"
