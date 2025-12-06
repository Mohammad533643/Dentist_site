from django.apps import AppConfig


class DentistInfoAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dentist_info_app"

    def ready(self):
        import dentist_info_app.signals
