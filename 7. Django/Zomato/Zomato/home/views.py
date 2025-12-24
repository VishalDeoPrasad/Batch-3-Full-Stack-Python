from django.shortcuts import render, HttpResponse
from home.models import Register

# Create your views here.
def home(request):
    return HttpResponse("This is my home page!")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = Register.objects.filter(
            username=username, 
            password=password).first()
        if user:
            return HttpResponse("Login Successful!")
        else:
            return HttpResponse("Invalid Username or Password")

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')

        Register.objects.create(
            username=username,
            name=name,
            mobile=mobile,
            email=email,
            password=password
        )
        return HttpResponse("User Registered Successfully!")
        
    return render(request, 'register.html')