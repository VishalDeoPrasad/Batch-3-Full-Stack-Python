from django.shortcuts import render, HttpResponse
from home.models import UserInfo

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password =  request.POST.get('password')
        #print(email, password)
        
        user = UserInfo.objects.filter(email=email, password=password).first()
        if user:
            return HttpResponse("Welcome Back! Login Successful!")
        else:
            return HttpResponse("Login Failed, No User Found!")
        
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
       name = request.POST.get('fullname')
       email = request.POST.get('email')
       display_name = request.POST.get('displayname')
       contact = request.POST.get('contact')
       city = request.POST.get('city')
       dob = request.POST.get('date')
       password =  request.POST.get('password')
       #print(name, email, display_name, contact, city, dob, password)   

       UserInfo.objects.create(
           name = name,
           email = email,
           display_name = display_name,
           contact = contact,
           city = city,
           date_of_birth = dob,
           password = password
       )
       
    return render(request, 'register.html')