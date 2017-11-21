from django.contrib import admin
from .models import ReviewSites, Monthly


#All Reviews
class ReviewSitesModelAdmin(admin.ModelAdmin):
    list_display = ["review", "sentiment", "site", "rate",  "month", "day", "year",]
    list_filter = ["month", "year", "sentiment", "site"]
    search_fields = ["site", "sentiment"]
    class Meta:
        model = ReviewSites

admin.site.register(ReviewSites, ReviewSitesModelAdmin)


#All Montly Reviews
class MonthlyModelAdmin(admin.ModelAdmin):
    list_display = ["month", "year", "total_pos", "total_neg"]
    list_filter = ["month", "year"]
    search_fields = ["month", "year"]
    class Meta:
        model = Monthly

admin.site.register(Monthly, MonthlyModelAdmin)