from django import forms

from .models import (
    Companion,
    ProfilePage,
)

class ProfilePageCreateForm(forms.ModelForm):
    class Meta:
        model = ProfilePage
        fields = [
            'evacuation_status'
        ]


class CompanionCreateForm(forms.ModelForm):
    class Meta:
        model = Companion
        fields = [
            'first_name',
            'last_name',
            'relationship_type',
        ]