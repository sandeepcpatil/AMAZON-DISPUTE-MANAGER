from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["order_id", "item_name", "customer_name", 'order_amount']
