from django.shortcuts import render

# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        description = request.POST.get("description")
        context = {
            "name" : name, 
            "mobile" : mobile,
            "email" : email,
            "description": description
        }
        return render(request, "result.html", context)
    return render(request, 'contact.html')