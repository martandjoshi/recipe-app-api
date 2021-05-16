from django.http import HttpResponse


def index(request):
    output = 'Sonthing Awesome'
    return HttpResponse(output)
