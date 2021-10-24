from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.html import escape
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'user',  'phone_1', 'phone_2',)
    list_display_links = ('user',)
    search_fields = ('user', 'phone_1', 'phone_2',)
    list_per_page = 10
    #readonly_fields = ('image_preview',)
