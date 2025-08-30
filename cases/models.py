from django.db import models
from orders.models import Order
from returns.models import Return


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
