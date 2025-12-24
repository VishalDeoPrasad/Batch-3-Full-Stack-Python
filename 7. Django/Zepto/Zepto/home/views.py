from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my home page!")

def about(request):
    return HttpResponse("This is my About Page!")

def services(request):
    return HttpResponse("This is my Services Page!")

def contact(request):
    return HttpResponse("This is my contact page!")

def gallary(request):
    return HttpResponse("This is my Gallary Page!")