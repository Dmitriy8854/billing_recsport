import os
from celery import Celery


os.environ.setdefaultet("DJANGO_SETTINGS_MODULE", "billing.settings")

app = Celery("billing")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task
def hello(invoice_id):
    return "hello world"
