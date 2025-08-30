from django import forms
from .models import Return


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ["order", "return_reason", "tracking_id"]
