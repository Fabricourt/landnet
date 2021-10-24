from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from PIL import Image

class Realtor(models.Model):
  name = models.CharField(max_length=200, blank=True, null=True)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  bio = RichTextField(blank=True, null=True)
  office = models.CharField(max_length=200, blank=True)
  fax = models.CharField(max_length=20, blank=True)
  whatsapp = models.CharField(max_length=20, blank=True)
  mobile = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.name

  def image_tag(self):
      return mark_safe('<img src="%s" width="65px" height="65px" />'%(self.photo.url))
      image_tag.short_description = 'Image'