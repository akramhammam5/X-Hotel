from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactMessage


def Admin(request):
    return render(request, 'admin.html')
def login_signup_view(request):
    return render(request, 'Register.html')

def Home(request):
    return render(request, 'Home.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Check if the name already exists in the database
            if ContactMessage.objects.filter(name=name).exists():
                return HttpResponse("This name has already been used. Please provide a different name.", status=400)
            
            # Create a new ContactMessage instance if the name is not redundant
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            return redirect('contact_success')
        else:
            return HttpResponse("Please fill out all fields.", status=400)
    
    return render(request, 'index.html')

def contact_success_view(request):
    messages = ContactMessage.objects.all()
    return render(request, 'success.html', {'messages': messages})
