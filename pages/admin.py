from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import escape
from .models import *





@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title',  'about', 'service', 'faq', 'policy', 'home', 'core', 'mvp',  'published', 'privacy', 'cookies', )
    list_display_links = ('title',)
    list_filter = ('updated', 'about', 'service', 'home', 'core', 'mvp',   'faq', 'policy', 'privacy', 'cookies',  'published',)
    list_editable = ( 'about', 'service', 'faq', 'core', 'policy', 'privacy', 'cookies', 'home', 'mvp',  'published',)
    search_fields = ('title',)
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
        ('Orders', {'fields': ['cssorder', 'mvp', 'home', 'about', 'service', 'faq', 'policy', 'privacy', 'cookies', 'core',], 'classes': ['pretty',], },),
        ('Metatag', {'fields': ['meta_keywords', 'meta_description', 'meta_title', ], 'classes': ['pretty',], },),
        ('Metagraph', {'fields': ['meta_ogurl', 'meta_ogtitle', 'meta_ogimage', 'meta_ogimagealt'], 'classes': ['pretty',], },),
        ('Metatwitter', {'fields': ['meta_twittersite', 'meta_twittercard', 'meta_twitterimagealt', 'meta_twitterimage', ], 'classes': ['pretty',], },),
        ('Publish', {'fields': ['published',], 'classes': ['pretty',], },),
    
     
    ]