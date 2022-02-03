from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import escape
from .models import *





@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title',  'about', 'service', 'faq', 'policy', 'home', 'mvp',  'published', )
    list_display_links = ('title',)
    list_filter = ('updated', 'about', 'service', 'home', 'mvp', 'faq', 'policy',  'published',)
    list_editable = ( 'about', 'service', 'faq',  'policy', 'home', 'mvp',  'published',)
    search_fields = ('title',)
    #list_filter = ( 'about', 'service', 'home',)
    list_editable = ( 'about', 'service', 'faq',  'policy', 'home', 'mvp',  'published',)
    search_fields = ('title',)
    #list_filter = ( 'about', 'service', 'home',)
    list_editable = ( 'about', 'service', 'faq',  'policy',  'home', 'mvp',  'published',)
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('realtor',)
    date_hierarchy = 'updated'
    #ordering = ('published', 'updated')
    list_per_page = 10
    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

    fieldsets = [
        ('Meta', {'fields': ['title', 'slug',], 'classes': ['pretty',], },),
        ('About', {'fields': ['description',], 'classes': ['pretty',], },),
        ('Media', {'fields': ['photo', 'youtube',], 'classes': ['pretty',], },),
        ('Orders', {'fields': ['linked', 'cssorder', 'mvp', 'home', 'about', 'service', 'faq', 'policy'], 'classes': ['pretty',], },),
        ('Metatag', {'fields': ['meta_keywords', 'meta_description', 'meta_title', ], 'classes': ['pretty',], },),
        ('Publish', {'fields': ['draft', 'published',], 'classes': ['pretty',], },),
    
     
    ]