from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return HttpResponse("This is my Home page!")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        description = request.POST.get("description")

        Contact.objects.create(
            name = name,
            mobile = mobile,
            email = email, 
            description = description
        )  

    return render(request, 'contact.html')