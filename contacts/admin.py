from django.contrib import admin

from .models import *

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'listing', 'phone', 'pick_date', 'contact_date')
  list_display_links = ('id', 'name', 'listing',)
  list_filter = ('pick_date', 'contact_date',)
  search_fields = ('name', 'phone', 'listing')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)

class ContactusAdmin(admin.ModelAdmin):
  list_display = ('name', 'header', 'phone', 'timestamp',)
  list_display_links = ('header', 'name',)
  list_filter = ('timestamp',)
  search_fields = ('name', 'header', 'phone', )
  list_per_page = 25

admin.site.register(Contactus, ContactusAdmin)