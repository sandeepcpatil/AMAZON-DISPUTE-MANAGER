from django import forms
from .models import Return


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ["order", "return_reason", "tracking_id", 'return_data']
        widgets = {
            "return_data": forms.DateInput(attrs={"type": "date"})  # HTML5 date picker
        }
