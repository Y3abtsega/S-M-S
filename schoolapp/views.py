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

def grades(request):

    global result1, context
    data_load = AddGrade.objects.get(pk=2)
    data_pick = data_load.file
    data = pandas.read_csv(data_pick)


    c_1 = data['Test_1'].to_list()
    print(c_1)
    resulte = c_1[0]
    resultm = c_1[1]
    resulth = c_1[2]
    resultb = c_1[3]
    resultc = c_1[4]
    resultp = c_1[5]

    c_2= data['Test_2'].to_list()
    print(c_2)
    result1e = c_2[0]
    result1m = c_2[1]
    result1h = c_2[2]
    result1b = c_2[3]
    result1c = c_2[4]
    result1p = c_2[5]

    c_3 = data['Mid_Exam'].to_list()
    print(c_3)
    result2e = c_3[0]
    result2m = c_3[1]
    result2h = c_3[2]
    result2b = c_3[3]
    result2c = c_3[4]
    result2p = c_3[5]
    c_4 = data['Assignment'].to_list()
    print(c_4)
    result3e = c_4[0]
    result3m = c_4[1]
    result3h = c_4[2]
    result3b = c_4[3]
    result3c = c_4[4]
    result3p = c_4[5]

    c_5 = data['Final_exam'].to_list()
    print(c_5)
    result4e = c_5[0]
    result4m = c_5[1]
    result4h = c_5[2]
    result4b = c_5[3]
    result4c = c_5[4]
    result4p = c_5[5]

    c_6 = data['Final_Grade'].to_list()
    print(c_6)
    result5e = c_6[0]
    result5m = c_6[1]
    result5h = c_6[2]
    result5b = c_6[3]
    result5c = c_6[4]
    result5p = c_6[5]



    context = {
        # c_1
        'resulte':resulte,
        'resultm':resultm,
        'resulth':resulth,
        'resultb':resultb,
        'resultc':resultc,
        'resultp':resultp,
        # c_2
        'result1e': result1e,
        'result1m': result1m,
        'result1h': result1h,
        'result1b': result1b,
        'result1c': result1c,
        'result1p': result1p,
        #c_3
        'result2e': result2e,
        'result2m': result2m,
        'result2h': result2h,
        'result2b': result2b,
        'result2c': result2c,
        'result2p': result2p,
        #c_4
        'result3e': result3e,
        'result3m': result3m,
        'result3h': result3h,
        'result3b': result3b,
        'result3c': result3c,
        'result3p': result3p,
        #c_5
        'result4e': result4e,
        'result4m': result4m,
        'result4h': result4h,
        'result4b': result4b,
        'result4c': result4c,
        'result4p': result4p,

        #c_6
        'result5e': result5e,
        'result5m': result5m,
        'result5h': result5h,
        'result5b': result5b,
        'result5c': result5c,
        'result5p': result5p,
    }


    return render(request, 'school/grades.html', context=context)


