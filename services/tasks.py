from src.celery import app

from .utils import get_pay_status
from billing.models import Order, OrderStatus


@app.task
def pay_status():
    # get_pay_status(invoice_id)
    payments = Order.objects.filter(status=OrderStatus.CREATE.value)
    for pay in payments:
        if get_pay_status(pay.invoice_id) == "paid":
            pay.status = OrderStatus.SUCCESS.value
            pay.save()
        if get_pay_status(pay.invoice_id) == "expired":
            pay.status = OrderStatus.CANCEL.value
            pay.save()


#  paid, expired
