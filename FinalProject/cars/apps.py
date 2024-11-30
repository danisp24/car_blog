from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FinalProject.cars'

    def ready(self):
        import FinalProject.cars.signals
