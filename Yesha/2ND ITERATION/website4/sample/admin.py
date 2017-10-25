from django.contrib import admin
from .models import ReviewSites

class ReviewSitesModelAdmin(admin.ModelAdmin):
    list_display = ["review", "sentiment", "site", "rate",  "month", "day", "year",]
    list_filter = ["month", "year", "sentiment", "site"]
    search_fields = ["site", "sentiment"]
    class Meta:
        model = ReviewSites

admin.site.register(ReviewSites, ReviewSitesModelAdmin)
