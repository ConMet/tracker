from django.apps import AppConfig
from django.conf import settings


class ScrapeConfig(AppConfig):
    name = 'scrape'

    def ready(self):
        from scrape.schedule import scheduler
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
