from django.shortcuts import render, HttpResponse

users = {
    'vishalkumar':'12345',
    'admin':'22222',
    'amitkumar': '11111'
}

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username in users and users[username] == password:
            return HttpResponse("Login Successful!")
        else:
            return HttpResponse("Login Failed!")
    return render(request, 'login.html')