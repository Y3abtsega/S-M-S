from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Name
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
            return redirect('register')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return HttpResponse("Successfully registered")
    return render(request, 'register.html')



def login_page(request) :

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.WARNING, 'This is a warning message.')

    return render(request, 'login_page.html')


def dashboard(request) :
    return render(request, 'dashboard.html')

def Grades(request) :
    name = Name.objects.first()
    return render(request, 'Grades.html', {'name': name})


def Calender(request) :
    return render(request, 'Calender.html')

def Chat(request) :
    return render(request, 'Chat.html')

# teacher's grade table code goes here ...

def tgrade(request) :

    return render(request, 'teacher grade table.html')