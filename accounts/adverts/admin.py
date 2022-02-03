from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import escape
from .models import *

"""
@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('label', 'listing', 'ad_date', 'is_published',)
    list_display_links = ('label',)
    list_filter = ('listing',  'is_published', 'ad_date' )
    list_editable = ( 'listing', 'is_published',)
    search_fields = ('label', 'listing',)
    list_per_page = 10
    #readonly_fields = ('image_preview',)
"""
