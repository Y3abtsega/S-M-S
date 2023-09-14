from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='loginpage'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Grades/', views.Grades, name='Grades'),
    path('Calender/', views.Calender, name='Calender'),
    path('Chat/', views.Chat, name='Chat'),
]