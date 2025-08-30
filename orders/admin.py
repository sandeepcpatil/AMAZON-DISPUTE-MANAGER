from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_id",
        "item_name",
        "customer_name",
        "order_data",
        "order_amount",
    )
    search_fields = (
        "order_id",
        "item_name",
        "customer_name",
        "customer_email",
        "asin",
    )
