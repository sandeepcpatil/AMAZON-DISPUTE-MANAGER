from django import forms
from .models import DisputeCase, Order, Return

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["order_id", "item_name", "customer_name"]

class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ["order", "return_reason", "tracking_id"]

class DisputeCaseForm(forms.ModelForm):
    class Meta:
        model = DisputeCase
        fields = ["returns", "reason_code", "status"]
