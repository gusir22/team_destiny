from django import forms

from .models import (
    Companion
)


class CompanionCreateForm(forms.ModelForm):
    class Meta:
        model = Companion
        fields = [
            'first_name',
            'last_name',
            'relationship_type',
        ]