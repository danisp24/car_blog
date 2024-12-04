from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now, is_naive, make_aware

from .models import Car, TestDriveBooking


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'category', 'price', 'description',
                  'available_for_test_drive']


class CarCreateForm(CarBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class TestDriveBookingForm(forms.ModelForm):
    class Meta:
        model = TestDriveBooking
        fields = ['car', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'car': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(available_for_test_drive=True)

    def clean(self):
        cleaned_data = super().clean()
        car = cleaned_data.get('car')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            combined_datetime = datetime.combine(date, time)
            if is_naive(combined_datetime):
                combined_datetime = make_aware(combined_datetime)
            if combined_datetime < now():
                raise ValidationError("The selected date and time cannot be in the past.")

        if car and TestDriveBooking.objects.filter(car=car, status='Confirmed').exists():
            raise ValidationError(f"The car {car.brand} already has a confirmed booking.")

        return cleaned_data
