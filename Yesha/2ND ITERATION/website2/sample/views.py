from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is the sample app </h1>")


def submit(request):
    info=request.POST['info']