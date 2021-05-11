from django.db import models

class Team(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  role=models.CharField(max_length=50)
  fb_link=models.CharField(max_length=255)
  insta_link=models.CharField(max_length=255)
  yt_link=models.CharField(max_length=255, default="https://www.youtube.com/")
  photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.first_name
  


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

