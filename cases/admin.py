from django.contrib import admin
from .models import Order, Return, DisputeCase

# Register your models here.






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
