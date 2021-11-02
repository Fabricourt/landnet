from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page_id>', views.page, name='page'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('underconstruction', views.underconstruction, name='underconstruction')
]
