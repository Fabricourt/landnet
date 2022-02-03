from django.urls import path
from  . import views
from django.contrib.sitemaps.views import sitemap
from . sitemap import *
from listings . sitemap import *

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page_id>', views.page, name='page'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('underconstruction', views.underconstruction, name='underconstruction'),
    path('sitemap.xml', sitemap, {'sitemaps': {'page' : PageSitemap, 'listing' : ListingSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
]
