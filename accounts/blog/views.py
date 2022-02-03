from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def blog_posts(request):
  return render(request, 'blog/blog_posts.html')

def blog_post(request):
  return render(request, 'blog/blog_post.html')