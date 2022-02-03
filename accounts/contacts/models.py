from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Contact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  pick_date = models.DateTimeField(blank=True, null=True)
  contact_date = models.DateTimeField(default=timezone.now)
  user_id = models.IntegerField(blank=True)

  class Meta:
    verbose_name = 'Customers-message'
    verbose_name_plural = 'Customers-messages'
    ordering = ('-contact_date',)

  def __str__(self):
    return self.name


# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    header = models.CharField(max_length=300, blank=True, null=True )
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)    
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Contactus'
        verbose_name_plural = 'Contactus'
        ordering = ('-timestamp',)

    def __str__(self):
        return self.name