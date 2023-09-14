from django.shortcuts import render
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
        user = authenticate(request, user_name=user_name, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect(reverse('school:dashboard'))
        # else:
        #     return render(request, 'school/login.html', {'error': 'Invalid credentials'})
        user1 = Parents.objects.get(user_name=user_name)
        if user1.password  ==password:
            return redirect(request, 'school/dashboard.html')
        else:
            return render(request, 'school/dashboard.html', {'error': 'Invalid credentials'})
    return render(request, 'scho'
                           'ol/login.html')
def grades(request):
    subject = models.Subject.objects.all()
    context = {'subjects': subject}

    name = 'aaaa'
    return render(request,'subject_grade/grade.html',context=context, name = name)