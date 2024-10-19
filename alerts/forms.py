from django import forms

from .models import (
    Alert,
    AlertUpdate,
)


class AlertCreateForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = [
            'title',
            'description',
            'status',
        ]
        

class AlertUpdateCreateForm(forms.ModelForm):
    class Meta:
        model = AlertUpdate
        fields = [
            'description',
        ]
        