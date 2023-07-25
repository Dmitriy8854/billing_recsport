from src.celery import app

from .utils import get_pay_status


@app.task
def pay_status(invoice_id):
    return "status"
    pass
