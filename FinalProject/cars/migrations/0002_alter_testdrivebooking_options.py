# Generated by Django 5.1.3 on 2024-11-30 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testdrivebooking',
            options={'permissions': [('manage_bookings', 'Can manage test drive bookings')]},
        ),
    ]
