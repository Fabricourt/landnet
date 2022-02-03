from django.contrib.sitemaps import Sitemap
from .models import Page
from listings.models import Listing
from django.urls import reverse
  
class ListingSitemap(Sitemap):
    def items(self):
        return Listing.objects.all()
        
    def lastmod(self, obj):
        return obj.list_date
    
    def location(self,obj):
        return '/listing/%s' % (obj.slug)

  
class PageSitemap(Sitemap):
    def items(self):
        return Page.objects.all()
        
    def lastmod(self, obj):
        return obj.updated
    
    def location(self,obj):
        return '/page/%s' % (obj.slug)

