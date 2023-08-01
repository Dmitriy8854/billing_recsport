import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
app = Celery("billing")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# @app.task
# def hello(invoice_id):
#     return "hello world"

app.conf.beat_schedule = {
    "status_pay_1_minute": {
        "task": "services.tasks.pay_status",
        "schedule": crontab(minute="*/1"),
    },
}
