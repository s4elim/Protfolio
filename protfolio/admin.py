from .models import Profile
from django.contrib import admin


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'mail', 'phone', 'created_at','upload')
    
admin.site.register(Profile, ProfileAdmin)