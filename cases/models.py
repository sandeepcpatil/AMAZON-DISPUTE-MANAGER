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


class DisputeCase(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("submitted", "Submitted to Amazon"),
        ("awaiting", "Awaiting Amazon Response"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("closed", "Closed"),
    ]

    REASON_CHOICES = [
        ("damaged", "Item is damaged"),
        ("wrong_item", "Wrong Item Sent"),
        ("no_return", "Not actually returned"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=255)
    order = models.ForeignKey(
        Order, related_name="cases", on_delete=models.SET_NULL, blank=True, null=True
    )
    returns = models.ManyToManyField(Return, related_name="cases", blank=True)
    reason_code = models.CharField(max_length=20, choices=REASON_CHOICES)
    details = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    amazon_case_id = models.CharField(max_length=100, blank=True)
    resolution_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Case {self.id} - {self.title}"
