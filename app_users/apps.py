from django.apps import AppConfig

class AppUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_users'

    def ready(self):
        from django.apps import apps
        Worker = apps.get_model('app_users', 'Worker')  # ✅ Bu yerda chaqiring

