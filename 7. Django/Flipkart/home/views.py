from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my Home page")

def about(request):
    return HttpResponse("This is my About Page")

def contact(request):
    return HttpResponse("This is my Contact Page")

def login(request):
    return HttpResponse("This is my Login Page")

def register(reqeust):
    return HttpResponse("This is my Register page")

