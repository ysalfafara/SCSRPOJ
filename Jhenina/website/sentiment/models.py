from django.db import models

# Create your models here.

class ReviewSite(models.Model):
    reviews = models.CharField(max_length=5000)
    rating_date = models.CharField(max_length=250)
    rating = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    sentiment = models.CharField(max_length=100)

    def __str__(self):
        return self.reviews + ' - ' + self.sentiment


