import os
from celery import Celery
from celery.schedules import crontab

# os.environ.setdefaultet("DJANGO_SETTINGS_MODULE", "billing.settings")

app = Celery("billing")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# @app.task
# def hello(invoice_id):
#     return "hello world"

app.conf.beat_schedule = {
    "status_pay_1_minute": {
        "task": "main.tasks.pay_status",
        "schedule": crontab(minute="*/1"),
    },
}
