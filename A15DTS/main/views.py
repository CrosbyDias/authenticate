from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    # Render the home page
    return render(request, 'main/home.html')

def about(request):
    print("Test the data",request.user.id)
    data = Student.objects.filter(user = request.user)
    return render(request, 'main/about.html', {'data': data})