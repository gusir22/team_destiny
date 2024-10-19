from django.contrib import admin

from .models import (
    Alert,
    AlertUpdate,
    ZipCode,
)


class ZipCodeAdmin(admin.ModelAdmin):
    model = ZipCode
    list_display = [
        'code',
    ]
    
admin.site.register(ZipCode, ZipCodeAdmin)


# Register your models here.
class AlertAdmin(admin.ModelAdmin):
    model = Alert
    list_display = [
        'title',
        'author',
        'status',
    ]
    
admin.site.register(Alert, AlertAdmin)


class AlertUpdateAdmin(admin.ModelAdmin):
    model = AlertUpdate
    list_display = [
        '__str__',
        'description',
    ]

admin.site.register(AlertUpdate, AlertUpdateAdmin)