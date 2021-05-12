from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):

  # Restricting user
  crew_choices = (
    ('Solo', 'Solo'),
    ('Small', 'Small'),
    ('Large', 'Large'),
  )

  camera_choices = (
    ('Canon', 'Canon'),
    ('Sony', 'Sony'),
    ('Nikon', 'Nikon'),
    ('Red', 'Red'),
    ('Fuji', 'Fuji'),
    ('Gopro', 'Gopro'),
    ('Other', 'Other'),
  )

  categories_choices = (
    ('Code', 'Code'),
    ('Mobile Review', 'Mobile Review'),
    ('Vlogs', 'Vlogs'),
    ('Comedy', 'Comedy'),
    ('Gaming', 'Gaming'),
    ('Films', 'Films'),
    ('Cooking', 'Cooking'),
    ('Others', 'Others'),
  )

  name = models.CharField(max_length=50)
  price = models.IntegerField()
  photo = models.ImageField(upload_to='media/ytubers/%Y/%m/%d/')
  video_url = models.CharField(max_length=250)
  description = RichTextField()
  city = models.CharField(max_length=50)
  age = models.IntegerField()
  height = models.IntegerField()
  crew = models.CharField(choices=crew_choices , max_length=250)
  camera_type = models.CharField(choices=camera_choices, max_length=250)
  subs_count = models.CharField(max_length=250)
  category = models.CharField(choices=categories_choices, max_length=250)
  is_featured = models.BooleanField(default=False)
  created_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
      return self.name 
  