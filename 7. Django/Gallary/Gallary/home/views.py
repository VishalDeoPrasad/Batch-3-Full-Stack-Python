from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def show_image(request):
    return render(request, "show_image.html")