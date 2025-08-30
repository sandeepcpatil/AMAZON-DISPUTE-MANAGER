from django import forms
from .models import DisputeCase

class DisputeCaseForm(forms.ModelForm):
    class Meta:
        model = DisputeCase
        fields = ["returns", "reason_code", "status"]
