from django.apps import AppConfig


class InflowsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inflows"
    verbose_name = "fluxos de entrada"

    def ready(self):
        import inflows.signals
