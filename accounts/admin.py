from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',  'phone_1', 'phone_2',)
    list_display_links = ('user',)
    search_fields = ('user', 'phone_1', 'phone_2',)
    list_per_page = 10
    #readonly_fields = ('image_preview',)
