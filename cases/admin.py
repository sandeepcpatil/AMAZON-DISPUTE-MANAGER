from django.contrib import admin
from .models import Order, Return, DisputeCase

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


@admin.register(Return)
class ReturnAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "rma",
        "return_reason",
        "tracking_id",
        "received_condition",
        "return_data",
    )
    search_fields = ("rma", "order__order_id", "tracking_id", "return_reason")
    list_filter = ('return_reason',)


@admin.register(DisputeCase)
class DisputeCaseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
        "reason_code",
        "status",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "details")
    list_filter = ("status", "reason_code")
    filter_horizontal = ("returns",)
