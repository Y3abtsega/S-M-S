from django.shortcuts import render,redirect
from django.urls import reverse

def dashboard(request):
    return render(request, 'school/dashboard.html')
