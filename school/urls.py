"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('', include('schoolapp.urls')),
=======
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.log, name='login'),
    # Add other URLs as needed
>>>>>>> parent of db1b9a4 (added url)
]
