from django.contrib import admin
from .models import ReviewSites

class ReviewSitesModelAdmin(admin.ModelAdmin):
    list_display = ["review", "sentiment", "date", "site"]
    list_filter = ["site", "sentiment", "date"]
    search_fields = ["site", "sentiment"]
    class Meta:
        model = ReviewSites

admin.site.register(ReviewSites, ReviewSitesModelAdmin)
