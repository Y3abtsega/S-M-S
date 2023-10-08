from django.shortcuts import render,redirect
from django.urls import reverse

def dashboard(request):
    return render(request, 'school/dashboard.html')
def chat(request):
    return render(request, 'school/chat.html')

def calender(request):
    return render(request, 'school/calender.html')
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

def add_grade(request):

    if request.method == 'POST':

        subject = request.POST.get('subject')
        student_name = request.POST.get('student_name')
        file = request.FILES.get('file')
        
        # Create and save a new AddGrade instance in the database
        AddGrade.objects.create(subject=subject, student_name=student_name, file=file)
        
        return redirect('school:add_grade')

    return render(request, 'school/add_grade.html')

def login_teacher(request):
    if request.method == 'POST':

        user_name = request.POST.get('user_name', '')
        password = request.POST.get('password', '')
        user = Teacher.objects.get(user_name=user_name)
        if user.password==password:
            return redirect(reverse('school:add_grade'))
        else:
            return render(request, 'school/login_teacher.html', {'error': 'Invalid credentials'})

    return render(request, 'school/login_teacher.html')
    
