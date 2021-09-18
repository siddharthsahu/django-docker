from django.http import HttpResponse, HttpResponseServerError
import datetime
import random

from .tasks import sample_task


def sample_view(request):
    now = datetime.datetime.now()

    try:
        task = sample_task.delay(random.randint(1, 100))
        html = f"<html><body>Celery task with id {task.id} is triggered at {now}.</body></html>"
        return HttpResponse(html)

    except Exception as e:
        return HttpResponseServerError("Error encountered in triggering task")

