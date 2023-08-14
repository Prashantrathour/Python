from django.db import models

# Create your models here.
class PostCreate(models.Model):

    caption = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
