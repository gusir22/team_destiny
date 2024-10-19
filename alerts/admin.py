from django.contrib import admin

from .models import (
    Alert,
)

# Register your models here.
class AlertAdmin(admin.ModelAdmin):
    model = Alert
    list_display = [
        'title',
        'author',
        'status',
    ]
    
admin.site.register(Alert, AlertAdmin)
