from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import escape
from .models import *



admin.site.register(Feature)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'for_rs',  'plot', 'house', 'rental', 'mvp', 'is_published',)
    list_display_links = ('title',)
    list_filter = ('list_date', 'realtor', 'plot', 'house', 'rental', 'mvp',  'neighbourhood', 'town', 'county', 'is_published', 'list_date' )
    list_editable = ( 'for_rs', 'plot', 'house', 'rental', 'mvp', 'is_published',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('realtor',)
    date_hierarchy = 'list_date'
    ordering = ('is_published', '-list_date')
    list_per_page = 10
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


    fieldsets = [
        ('Title', {'fields': ['realtor', 'title', 'slug', 'price', 'map_link', 'for_rs', 'list_date', ], 'classes': ['pretty',],},),
        ('Property Location', {'fields': ['neighbourhood', 'town', 'county',], 'classes': ['pretty',],},),
        ('Select property', {'fields': ['plot', 'house', 'rental'], 'classes': ['pretty',],},),
        ('Plot here', {'fields': ['plot_type', 'plot_size', 'large_plot_size', 'soil_type', 'document_type',], 'classes': ['collapse',],},),
        ('House here', {'fields': ['sqft', 'bedrooms', 'bathrooms', 'garage', ], 'classes': ['collapse',],},),
        ('Property description', {'fields': ['description',], 'classes': ['pretty',],},),
        ('Photos', {'fields': ['photo_main',], 'classes': ['pretty',],},),
        ('Add more photos here', {'fields': ['photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6',], 'classes': ['collapse',],},),
        ('Publish', {'fields': ['mvp', 'is_published',], 'classes': ['pretty',],},),
    ]
