from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html') 

def lists(request):
    listings = seedStars.objects.all()
    return render(request, 'myapp/lists.html', {'listings': listings}) 

def add(request):
    if request.method == 'POST':
        # Get form values
        name = request.POST['name']
        email = request.POST['email']

        # If email exists
        if seedStars.objects.filter(email=email).exists():
            messages.error(request, 'The email is taken')
            return redirect('myapp:add')
        details = seedStars(name=name, email=email)
        details.save()
        return redirect('myapp:list')
        
    return render(request, 'myapp/add.html') 