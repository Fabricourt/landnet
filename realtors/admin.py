from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'user', 'mobile',  'email', 'is_mvp', 'hire_date')
  list_display_links = ('id', 'name',)
  list_editable = (  'is_mvp',)
  search_fields = ('user',)
  list_per_page = 25

  def image_preview(self, obj):
      return obj.image_preview

  image_preview.short_description = 'Image Preview'
  image_preview.allow_tags = True

admin.site.register(Realtor, RealtorAdmin)
