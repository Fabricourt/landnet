from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from PIL import Image
from django.template.loader import render_to_string
from ckeditor.fields import RichTextField
#from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation



class Feature(models.Model):
  label = models.CharField(max_length=200, unique=True, help_text="property features")

  class Meta:
    ordering = ('label',)


  def __str__(self):
    return self.label



PLOT_TYPE_CHOICES = (
    ('Beach', 'Beach'),
    ('Residential','Residential'),
    ('Commercial','Commercial'),
    ('Farm','Farm'),
    ('Ranch','Ranch'),
  )



HOUSE_TYPE_CHOICES = (
    ('Mansionnete', 'Mansionnete'),
    ('Bungalow','Bungalow'),
    ('Apartment','Apartment'),
    ('Studio','Studio'),
    ('Alcove Studio','Alcove Studio'),
    ('Convertible Studio','Convertible Studio'),
    ('Convertible Studio','Convertible Studio'),
    ('Duplex/Triplex','Duplex/Triplex'),
    ('Junior 1 Bedroom','Junior 1 Bedroom'),
    ('Garden Apartment','Garden Apartment'),
    ('Railroad Apartment','Railroad Apartment'),


  )

FOR_RS_CHOICES = (
  ('For rent', 'For rent'),
  ('For lease', 'For lease'),
  ('For Sale', 'For sale'),
)

DOCUMENT_CHOICES = (
  ('Title','Title'),
  ('Certificate','Certificate'),
  ('Agreement','Agreement'),
)


SOIL_TYPE_CHOICES = (
    ('Cotton Soil','Cotton Soil'),
    ('Red Soil','Red Soil'),
    ('Sand Soil','Sand Soil'),
    ('Brown soil','Brown Soil'),
  )

PLOT_SIZE_CHOICES = (
    ('40X80ft','40X80ft'),
    ('50X100ft','50X100ft'),
    ('100X100ft','100X100ft'),
    ('1 Acre','1 Acre'),
    ('2 Acre','2 Acre'),
    ('3 Acre','3 Acre'),
    ('4 Acre','4 Acre'),
    ('5 Acre','5 Acre'),
    ('6 Acre','6 Acre'),
    ('7 Acre','7 Acre'),
    ('8 Acre','8 Acre'),
    ('9 Acre','9 Acre'),
    ('10 Acre','10 Acre'),
  )




class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  slug = models.SlugField(blank=True, null=True)
  neighbourhood = models.CharField(max_length=200)
  town = models.CharField(max_length=100)
  county = models.CharField(max_length=100)
  description = RichTextField(blank=True, null=True)
  features = models.ManyToManyField(Feature, related_name='listings')
  price = models.IntegerField()
  house_type = models.CharField(max_length=100,
                              choices=HOUSE_TYPE_CHOICES, blank=True, null=True
                             )
  for_rs = models.CharField(max_length=100,
                              choices=FOR_RS_CHOICES, blank=True, null=True
                             )
  plot_type = models.CharField(max_length=100,
                              choices=PLOT_TYPE_CHOICES, blank=True, null=True
                              )

  soil_type = models.CharField(max_length=100,
                              choices=SOIL_TYPE_CHOICES, blank=True, null=True
                              )

  plot_size = models.CharField(max_length=100,
                              choices=PLOT_SIZE_CHOICES, blank=True, null=True
                              )
  document_type = models.CharField(max_length=100,
                              choices=DOCUMENT_CHOICES, blank=True, null=True
                              )
  large_plot_size = models.IntegerField(default=0, null=True, blank=True, help_text='state number of acres ..only for plots larger than 10acres')
  bedrooms = models.IntegerField(default=0, blank=True, null=True)
  bathrooms = models.IntegerField(default=0, blank=True, null=True)
  garage = models.IntegerField(default=0, blank=True, null=True)
  sqft = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  sold = models.BooleanField(default=False)
  rental = models.BooleanField(default=False)
  house = models.BooleanField(default=False)
  plot = models.BooleanField(default=False)
  mvp = models.BooleanField(default=False)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  map_link = models.URLField(max_length=200, null=True, blank=True)


@property
def image_preview(self):
    if self.photo_main:
        return mark_safe('<img src="{}" width="80" height="80" />'.format(self.photo_main.url))
    return ""


def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    return super(Listing, self).save(*args, **kwargs)

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('listing',  args=[str(self.id)])





class Wishlist(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)# here CASCADE is the behavior to adopt when the referenced object(because it is a foreign key) is deleted. it is not specific to django,this is an sql standard.
  wished_item = models.ForeignKey(Listing,on_delete=models.CASCADE)
  added_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.wished_item.title
