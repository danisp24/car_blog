# Generated by Django 5.1.3 on 2024-12-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_testdrivebooking_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_url',
            field=models.URLField(default='https://t3.ftcdn.net/jpg/07/31/17/02/360_F_731170296_Xamy0xpnprlowd7SPEIMHZqTWxJGRqHv.jpg'),
        ),
    ]