from django.shortcuts import render, HttpResponse
from home.models import Register

# Create your views here.
def home(request):
    return HttpResponse("This is my home page!")

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(username, name, mobile, email, password)

        data = Register(
            name=name,
            username=username,
            mobile=mobile,
            email=email,
            password=password
        )
        data.save()

    return render(request, 'register.html')