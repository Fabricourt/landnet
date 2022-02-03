
from django.urls import path

from . import views

urlpatterns = [
  path('contact', views.contact, name='contact'),
  path('contactus', views.contactus, name='contactus'),
  path("thanks", views.thanks, name="thanks"),
]
