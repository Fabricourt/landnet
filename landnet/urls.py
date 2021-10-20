from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('listings/', include('listings.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
