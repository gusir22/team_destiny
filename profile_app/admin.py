from django.contrib import admin

from .models import (
    ProfilePage,
)
# Register your models here.
class ProfilePageAdmin(admin.ModelAdmin):
    model = ProfilePage
    list_display =[
        'user',
        'evacuation_status',
    ]
    
    
admin.site.register(ProfilePage, ProfilePageAdmin)
