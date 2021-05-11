from django.db import models

# Create your models here.
# This Silder will appear in admin panel and in db
class Slider(models.Model):
  headline = models.CharField(max_length=255)
  subtitle = models.CharField(max_length=255)
  button_txt = models.CharField(max_length=20)
  photo = models.ImageField(upload_to='media/slider/%Y/%m/')
  created_date = models.DateTimeField(auto_now_add=True)
  btn_link = models.URLField(max_length=200, default="https://www.google.com")

  def __str__(self):
      return self.headline  
