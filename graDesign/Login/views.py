from django.shortcuts import render, HttpResponse, redirect
from .models import students
from Manager.models import managers
import Manager.urls

# Create your views here.


# 学生登陆
def login(request):
    if request.method == 'POST':
        studentId = request.POST.get('studentId')
        password = request.POST.get('password')
        try:
            student = students.objects.get(
                studentId=studentId, password=password)
            if student:
                print('登录成功！')
                request.session['id'] = student.id
                return redirect('../../system/index/')
            else:
                print('登录失败！')
        except:
            print('登录失败！')
    return render(request, 'login/login.html')


# 管理员登陆
def admin(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        try:
            manager = managers.objects.get(account=account, password=password)
            print('manager', manager.manager)
            if manager:
                print('登录成功！')
                request.session['manager'] = manager.manager
                return redirect('../../manager/index/')
            else:
                print('登录失败！')
        except:
            print('登录失败！')
    return render(request, 'login/admin.html')
