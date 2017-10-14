from django.db import models

class ReviewSites(models.Model):
    site = models.CharField(max_length=15)
    review = models.CharField(max_length=5000)
    date = models.DateField()
    sentiment = models.CharField(max_length=5)

    def __str__(self):
        return self.review

