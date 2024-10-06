from django.shortcuts import render



# Create your views here.
def all_product(request):
    return render(request,'jinja/all_learningJinja.html')
    # return HttpResponse("<h1>Hello world!</h1>")