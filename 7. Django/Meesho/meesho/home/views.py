from django.shortcuts import render, HttpResponse, redirect
from home.models import Users

# Create your views here.
def home(request):
    return HttpResponse("This is my home page!")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Users.objects.get(user_email=email, user_password=password)
            request.session['user_id'] = user.user_id
            return redirect('dashboard')
        except:
            return render(request, 'login.html', {'error':'Invalid Credentials'})

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        displayname = request.POST.get('displayname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        city = request.POST.get('city')
        date = request.POST.get('date')
        password = request.POST.get('password')
        image = request.FILES['image']

        Users.objects.create(
            user_name = fullname,
            user_email = email,
            user_display_name = displayname,
            user_contact = contact,
            user_city = city,
            user_date_of_birth = date,
            user_password = password,
            user_image = image
        )

    return render(request, 'register.html')

def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    user = Users.objects.get(user_id=user_id)
    return render(request, 'dashboard.html', {'user': user})