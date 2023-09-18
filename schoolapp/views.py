from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
<<<<<<< HEAD
from .models import Name
=======
from .models import Subjects
>>>>>>> c40d881 (second iteration)
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
<<<<<<< HEAD
    name = Name.objects.first()
    return render(request, 'Grades.html', {'name': name})

=======
    return render(request, 'Grades.html')

def Grades(request):
    subject = Subjects.objects.all()
    context = {'subjects': subject}
    return render(request,'Grades.html',context=context)
>>>>>>> c40d881 (second iteration)

def Calender(request) :
    return render(request, 'Calender.html')

def Chat(request) :
    return render(request, 'Chat.html')