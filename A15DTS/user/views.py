from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import *



# Create your views here.
def login(request):
    if request.method == 'POST':    
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/home')
        else:
            error_message = 'Invalid username or password'
            return render(request,'athen/login.html', {'error_message': error_message})
    return render(request, 'athen/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')



# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         # phone = request.POST['phone']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm']

#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'User created successfully!')
#             return redirect('login')
#         else:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             user.save()
#             messages.success(request, 'User created successfully!')
#             return redirect('login')
        
#     return render(request, 'athen/register.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        # phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm']
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)  #User.objects.create_user  {ORM}<----- *important*
            user.save()
            messages.success(request, 'User created successfully!')
            return redirect('login')
    return render(request, 'athen/register.html')

# def forgot(request):
#     if request.method == 'PUT':                                                                                 We dont use PUT method in django there is only POST, GET and Files
#         username = request.PUT['username']
#         # email = request.PUT['email']
#         # phone = request.PUT['phone']
#         password = request.PUT['new_password']                                                                 This block of code is wrong!! The right code is below.
#         confirm_password = request.PUT['new_confirm']                                                          
#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match!')
#             return redirect('forgot')
#         else:
#             if User.objects.filter(username=username).exists():
#                 user = User.objects.update(password=password)
#                 user.save()
#                 messages.success(request, 'Password updated successfully!')
#             else:
#                 messages.error(request, 'User does not exist!')
#                 return redirect('forgot')
#     return render(request, 'athen/forgot.html')
def forgot(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['new_password']
        confirm_password = request.POST['new_confirm']

        if password != confirm_password:
            messages.error(request,"Password do not match")
            return redirect('forgot')
        
        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            messages.success(request,'Password updated succesfully')
            return redirect('login')
        except user.DoesNotExist:
            messages.error(request," User does not exit!")
            return redirect('forgot')
    
    return render(request,'athen/forgot.html')



def personal(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']   
        standard = request.POST['standard']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        address = request.POST['address']
        # dob = request.POST['dob']
        current_user = request.user 

        student = Student.objects.create(
            user=current_user,
            name = name,
            email = email,
            phone = phone,
            standard = standard,
            father_name = father_name,
            mother_name = mother_name,
            address = address,
            # dob = dob,
        )

        # params = request.POST                                # <-----  Shortest way to write the code
        # del params['csrfmiddlewaretoken']
        # print(params)
        
        # student = Student.objects.create(                    # <-----  Shortest way to write the code      
        #     **params                                         # <-----  Shortest way to write the code     
        # )
        # student = Student()             <-- this is the other way                     # <-----  Shortest way to write the code  
        # student.name = name                                  # <-----  Shortest way to write the code              
        # student.save()
    return render(request,'athen/personal.html')


