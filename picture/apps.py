from django.apps import AppConfig




class PictureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'picture'

    def ready(self):
        import picture.utils

