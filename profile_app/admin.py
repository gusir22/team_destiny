from django.contrib import admin

from .models import (
    ProfilePage,
    Companion,
)


class CompanionAdmin(admin.ModelAdmin):
    model = Companion
    list_display = [
        '__str__',
    ]
    

admin.site.register(Companion, CompanionAdmin)
    
    
# Register your models here.
class ProfilePageAdmin(admin.ModelAdmin):
    model = ProfilePage
    list_display =[
        'user',
        'evacuation_status',
    ]
    
    
admin.site.register(ProfilePage, ProfilePageAdmin)
