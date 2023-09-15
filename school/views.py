from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate,login
from .models import Parents



# Create your views here.



def dashboard(request):
    return render(request, 'school/dashboard.html')


def log(request):
    if request.method == 'POST':

        user_name = request.POST.get('user_name', '')
        password = request.POST.get('password', '')
        user = Parents.objects.get(user_name=user_name)
        if user.password==password:
            return redirect(reverse('school:dashboard'))
        else:
            return render(request, 'school/login.html', {'error': 'Invalid credentials'})
    return render(request, 'school/login.html')


def grades(request):
    return render(request, 'school/grades.html')


def chat(request):
    return render(request, 'school/chat.html')

def calender(request):
    return render(request, 'school/calender.html')