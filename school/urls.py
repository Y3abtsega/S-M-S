from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'school'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.log, name='login'),
    path('grades/', views.grades, name='grades'),
    path('chat/', views.chat, name='chat'),
    path('calender/', views.calender, name='calender'),

    # Add other URLs as needed
]
