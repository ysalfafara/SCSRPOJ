from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Taal Vista Sentiment Reviews</h1>")
