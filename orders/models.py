from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=30, unique=True)
    asin = models.CharField(max_length=20)
    item_name = models.CharField(max_length=255)
    customer_name = models.CharField(
        max_length=255,
        blank=True,
    )
    customer_email = models.EmailField(blank=True)
    order_data = models.DateTimeField(null=True, blank=True)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.order_id} - {self.item_name}"
