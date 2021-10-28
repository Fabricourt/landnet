from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import escape
from .models import *





@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title',  'about', 'service', 'faq', 'policy', 'privacy', 'cookies', 'home', 'mvp', 'published', )
    list_display_links = ('title',)
    list_filter = ('updated', 'about', 'service', 'home', 'mvp', 'faq', 'policy', 'privacy', 'cookies', 'published',)
    list_editable = ( 'about', 'service', 'faq', 'policy', 'privacy', 'cookies', 'home', 'mvp',  'published',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('realtor',)
    date_hierarchy = 'updated'
    #ordering = ('published', 'updated')
    list_per_page = 10
