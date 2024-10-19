# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        
        'last_name',
        'first_name',
        'is_superuser',
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('phone_number', 'street_address', 'city', 'zip_code', 'profile_photo',)
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)