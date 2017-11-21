from django.db import models


class ReviewSites(models.Model):
    site = models.CharField(max_length=15)
    review = models.TextField(max_length=5000)
    month = models.CharField(max_length=5)
    day = models.CharField(max_length=5)
    year = models.CharField(max_length=5)
    rate = models.CharField(max_length=5)
    sentiment = models.CharField(max_length=5)

    def __str__(self):
        return self.review


class Monthly(models.Model):
    month = models.CharField(max_length=5)
    year = models.CharField(max_length=5)
    total_pos = models.CharField(max_length=5)
    total_neg = models.CharField(max_length=5)

    def __str__(self):
        return self.month
