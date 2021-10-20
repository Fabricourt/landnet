from django.db import models
from realtors.models import Realtor
from datetime import datetime
from listings.models import Listing
from ckeditor.fields import RichTextField
from PIL import Image


class Advert(models.Model):
    label = models.CharField(max_length=200)
    photo = models.ImageField(default='default.jpg', upload_to='advert_pics')
    embed = RichTextField(blank=True, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True)
    ad_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
         return self.listing.title
