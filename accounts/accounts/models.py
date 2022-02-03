from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.html import mark_safe
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_1 = models.CharField(max_length=100, default='+000 000 000 000')
    phone_2 = models.CharField(max_length=100, blank=True, null=True, help_text="optional")
    whatsapp = models.CharField(max_length=20, blank=True)
    facebook = models.CharField(max_length=20, blank=True)
    twitter = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def image_tag(self):
      return mark_safe('<img src="%s" width="65px" height="65px" />'%(self.image.url))
      image_tag.short_description = 'Image'

def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.image.path)
