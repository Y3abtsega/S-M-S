from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'school'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.log, name='login'),
    # Add other URLs as needed
]
