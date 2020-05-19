from django.apps import AppConfig
from .views import sio

class ApiFetcherConfig(AppConfig):
    name = 'api_fetcher'

    def ready(self):
        from . import signals