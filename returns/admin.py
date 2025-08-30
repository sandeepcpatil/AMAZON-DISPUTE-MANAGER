from django.contrib import admin
from .models import Return

# Register your models here.


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
    list_filter = ("return_reason",)
