from django import forms
from .models import DisputeCase


class DisputeCaseForm(forms.ModelForm):
    class Meta:
        model = DisputeCase
        fields = ["title", "order", "returns", "reason_code", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["returns"].widget.attrs.update(
            {"class": "form-control", "size": "5"}
        )
