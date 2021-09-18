from os import environ

from celery import Celery
from django.conf import settings

environ.setdefault("DJANGO_SETTINGS_MODULE", "dockerapp.settings")


app = Celery("docker_celery", broker=environ.get("CELERY_BROKER_URL"))

app.config_from_object("django.conf:settings", namespace="CELERY")
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
