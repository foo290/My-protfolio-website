from django.shortcuts import render,HttpResponse

# Create your views here.
def projects_home(request):
    return HttpResponse('<h1>This is projects home</h1>')


