from django.db import models

class Home2(models.Model):
    image = models.ImageField(upload_to='home2/media')
    work_image = models.ImageField(upload_to='home2/media')
    title = models.CharField(max_length=20)
    sub_title = models.CharField(max_length=50)
    title_word =models.CharField(max_length=20)
    sub_title_word =models.CharField(max_length=50)