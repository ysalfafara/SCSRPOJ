from django.http import HttpResponse
from .models import ReviewSite

def index(request):
    all_ReviewSite = ReviewSite.objects.all()
    return HttpResponse('')

def detail(request, review_id):
    return HttpResponse("<h2>Wordcloud for Reviews: " + str(review_id) + "</h2>")

