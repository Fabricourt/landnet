from django.urls import path

from . import views

urlpatterns = [
    path('blog_posts', views.blog_posts, name='blog_posts'),
    path('blog_post', views.blog_post, name='blog_post'),
   # path('search', views.search, name='search')
]