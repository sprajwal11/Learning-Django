from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world!")

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")
