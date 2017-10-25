from django.http import HttpResponse
from .models import ReviewSite

def index(request):
    all_ReviewSite = ReviewSite.objects.all()
    html = ''
    for ReviewSite in all_ReviewSite:
        url = '/sentiment/' + str(ReviewSite.id) + '/'
        html += '<a href="' + url + ReviewSite.ReviewSite_reviews + '</a><br>'
    return HttpResponse(html)

def detail(request, review_id):
    return HttpResponse("<h2>Wordcloud for Reviews: " + str(review_id) + "</h2>")

