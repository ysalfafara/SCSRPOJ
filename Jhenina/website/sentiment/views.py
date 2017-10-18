from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Taal Vista Sentiment Reviews</h1>")

def detail(request, review_id):
    return HttpResponse("<h2>Wordcloud for Reviews: " + str(review_id) + "</h2>")