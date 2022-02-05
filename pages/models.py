from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
#from gallery.models import *
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.html import mark_safe
from django.template.loader import render_to_string
from datetime import datetime


CSSORDER = (
    ('active', 'active'),
    ('true','true'),
  )


class Page(models.Model):
    title = models.CharField(max_length=500, blank=False, null=True, unique=True, help_text='particular name of the area as known to the locals')
    slug = models.SlugField(max_length=250, unique_for_date='created')
    description = RichTextField(blank=True, null=True)
    photo =  models.ImageField(upload_to='Pages_photos/%Y/%m/%d/', default="landscape.jpg", blank=True,null=True, help_text="your image must be jpg format to save")
    youtube = models.TextField(blank=True, null=True)
    cssorder = models.CharField(max_length=100,
                                choices=CSSORDER, blank=True, null=True, help_text="for faq use true and for about use active"
                               )
    #video = models.FileField(upload_to='videos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    mvp = models.BooleanField(default=False)
    home = models.BooleanField(default=False)
    about = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    faq = models.BooleanField(default=False)
    policy = models.BooleanField(default=False)
    privacy = models.BooleanField(default=False)
    cookies = models.BooleanField(default=False)
    core = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    meta_keywords = models.CharField(max_length=200, blank=True, null=True, help_text="eg python, django, web, development")
    meta_description = models.CharField(max_length=500, blank=True, null=True, help_text="description")
    meta_title = models.CharField(max_length=200, blank=True, null=True, help_text="title ")
    meta_ogurl = models.CharField(max_length=200, blank=True, null=True, help_text="add a link to the leader like this https://janowski.dev/leader/2020/04/05/mpmwangi")
    meta_ogtitle = models.CharField(max_length=200, blank=True, null=True, help_text="interesting article title")
    meta_ogimage = models.CharField(max_length=200, blank=True, null=True, help_text="https://janowski.dev/static/cover.png")
    meta_ogimagealt = models.CharField(max_length=200, blank=True, null=True, help_text="a green cover image with django logo")
    meta_twittercard = models.CharField(max_length=200, blank=True, null=True, help_text="summary_large_image")
    meta_twittersite = models.CharField(max_length=300, blank=True, null=True, help_text="@MaciejJanowski")
    meta_twitterimage = models.CharField(max_length=200, blank=True, null=True, help_text="https/example.com/image.png")
    meta_twitterimagealt = models.CharField(max_length=200, blank=True, null=True, help_text="description of image")
    

    def image_tag(self):
        return mark_safe('<img src="%s" width="65px" height="65px" />'%(self.photo.url))
        image_tag.short_description = 'Image'


    class Meta:
        ordering = ('title',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.area)
        return super(Page, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
