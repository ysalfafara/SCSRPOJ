from django.db import models

# Create your models here.

class ReviewSite(models.Model):
    reviews = models.CharField(max_length=2000)
    ratingdate = models.CharField(max_length=250)
    rating = models.CharField(max_length=100)
    site = models.CharField(max_length=100)