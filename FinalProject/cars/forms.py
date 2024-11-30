from django import forms
from .models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'category', 'price', 'description',
                  'available_for_test_drive']


class CarCreateForm(CarBaseForm):
    pass
