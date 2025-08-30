from django.db import models

from orders.models import Order

# Create your models here.

class Return(models.Model):
    order = models.ForeignKey(Order, related_name="returns", on_delete=models.CASCADE)
    rma = models.CharField("Return ID", max_length=30, blank=True)
    return_reason = models.CharField(max_length=255, blank=True)
    tracking_id = models.CharField(max_length=100, blank=True)
    return_item_desc = models.TextField("Return Item", blank=True)
    received_condition = models.CharField(max_length=255, blank=True)
    return_data = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Return for ${self.order.order_id}, ({self.rma})"