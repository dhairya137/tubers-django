from django.db import models
from datetime import datetime

# Create your models here.
class Youtuber(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()
  photo = models.ImageField(upload_to='media/ytubers/%Y/%m/%d/')
  video_url = models.CharField(max_length=250)
  description = models.TextField()
  city = models.CharField(max_length=50)
  age = models.IntegerField()
  height = models.IntegerField()
  crew = models.CharField(max_length=250)
  camera_type = models.CharField(max_length=250)
  subs_count = models.CharField(max_length=250)
  category = models.CharField(max_length=250)
  is_featured = models.BooleanField(default=False)
  created_date = models.DateTimeField(default=datetime.now, blank=True)