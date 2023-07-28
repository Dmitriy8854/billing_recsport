from src.celery import app

from .utils import get_pay_status


@app.task
def pay_status(status):
    # get_pay_status(invoice_id)
    if get_pay_status(status) == "200":
        return True
    else:
        return False
    # return "status"
