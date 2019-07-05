from django.shortcuts import render, redirect, HttpResponse
from .models import booktype, books, managers
from Login.models import students
from System.models import borrowForm, returnForm
from django.db.models import Q
import datetime
# Create your views here.


# 返回管理员首页
def index(request):
    return render(request, 'manager/index.html')


# 查询图书
def inqbook(request):
    if request.method == 'POST':
        keyword = request.POST.get('key')
        print(keyword)
        bookList = books.objects.filter(Q(number__icontains=keyword) | Q(
            name__icontains=keyword) | Q(author__icontains=keyword))
        # print(bookList)
        return render(request, 'manager/inq_book.html', {'bookList': bookList})
    return render(request, 'manager/inq_book.html')


# 返回添加图书类型页面
def addstyle(request):
    return render(request, 'manager/add_style.html')


# 添加类型判断
def style(request):
    style = request.GET.get('booktype')
    print(style)
    style1 = booktype.objects.filter(style=style).first()
    if style1:
        print('已有该类型')
        a = HttpResponse('添加失败，已有该类型')

        a['Access-Control-Allow-Origin'] = "http://localhost:8000"

        # 允许你携带Content-Type请求头
        a['Access-Control-Allow-Headers'] = "*"
        return a
    else:
        print('添加成功')
        addstyle = booktype.objects.create(style=style)
        addstyle.save()
        a = HttpResponse('添加成功')

        a['Access-Control-Allow-Origin'] = "http://localhost:8000"

        # 允许你携带Content-Type请求头
        a['Access-Control-Allow-Headers'] = "*"
        return a


# 返回添加图书页面
def addbook(request):
    styleList = booktype.objects.all()
    style = []
    for style1 in styleList:
        style.append(style1.style)
    print(style)
    return render(request, 'manager/add_book.html', {'style': style})


# 添加图书判断
def addbooks(request):
    number = request.GET.get('number')
    name = request.GET.get('name')
    author = request.GET.get('author')
    style = request.GET.get('types')
    price = request.GET.get('price')
    press = request.GET.get('press')
    place = request.GET.get('place')
    stock = request.GET.get('stock')
    borrowedNum = request.GET.get('borrowedNum')
    types = booktype.objects.filter(style=style).first()
    print(types)
    if books.objects.filter(number=number).first():
        print('该图书编号已存在')
        a = HttpResponse('该图书编号已存在，请重新填写')

        a['Access-Control-Allow-Origin'] = "http://localhost:8000"

        # 允许你携带Content-Type请求头
        a['Access-Control-Allow-Headers'] = "*"
        return a
    else:
        print('添加成功')
        book = books.objects.create(number=number, name=name, author=author, style=types,
                                    price=price, press=press, place=place, borrowedNum=borrowedNum, stock=stock)
        book.save()
        a = HttpResponse('添加成功')

        a['Access-Control-Allow-Origin'] = "http://localhost:8000"

        # 允许你携带Content-Type请求头
        a['Access-Control-Allow-Headers'] = "*"
        return a


# 返回查询图书修改页面
def edit(request):
    return render(request, 'manager/edit_book.html')


# 判断修改图书编号是否存在
def editbooks(request):
    editNum = request.GET.get('editNum')
    book = books.objects.filter(number=editNum).first()
    print(book)
    if book:
        return HttpResponse('编号存在'.encode('utf8'))
    else:
        return HttpResponse('编号不存在'.encode('utf8'))


# 返回需要修改的图书信息
def editbook(request):
    number = request.GET.get('number')
    print(number)
    book = books.objects.filter(number=number).first()
    style1 = booktype.objects.filter(id=book.style_id).first()
    types = style1.style
    print('types', types)
    styleList = booktype.objects.all()
    style = []
    for style1 in styleList:
        style.append(style1.style)
    return render(request, 'manager/edit.html', {'book': book, 'style': style, 'types': types})


# 确定修改图书信息
def isedit(request):
    number = request.GET.get('number')
    name = request.GET.get('name')
    author = request.GET.get('author')
    style = request.GET.get('types')
    price = request.GET.get('price')
    press = request.GET.get('press')
    place = request.GET.get('place')
    stock = request.GET.get('stock')
    borrowedNum = request.GET.get('borrowedNum')
    types = booktype.objects.filter(style=style).first()
    book = books.objects.get(number=number)
    book.number = number
    book.name = name
    book.author = author
    book.style = types
    book.price = price
    book.place = place
    book.borrowedNum = borrowedNum
    book.stock = stock
    book.save()
    return HttpResponse('修改成功')


# 返回删除图书页面
def delbook(request):
    return render(request, 'manager/del_book.html')


# 判断需要删除的编号是否存在
def delbooks(request):
    editNum = request.GET.get('editNum')
    print(editNum)
    book = books.objects.filter(number=editNum).first()
    print(book)
    if book:
        return HttpResponse('编号存在'.encode('utf8'))
    else:
        return HttpResponse('编号不存在'.encode('utf8'))


# 返回需要删除的图书信息
def isdel(request):
    number = request.GET.get('number')
    print(number)
    book = books.objects.filter(number=number).first()
    style1 = booktype.objects.filter(id=book.style_id).first()
    types = style1.style
    print('types', types)
    return render(request, 'manager/del.html', {'book': book, 'types': types})


# 确定删除图书
def isdelbook(request):
    number = request.GET.get('number')
    print(number)
    books.objects.filter(number=number).delete()
    return HttpResponse('删除成功')


# 返回添加学生页面
def addstudent(request):
    return render(request, 'manager/add_student.html')


# 添加学生信息的判断
def addstudents(request):
    studentId = request.GET.get('studentId')
    password = request.GET.get('password')
    name = request.GET.get('name')
    gender = request.GET.get('gender')
    college = request.GET.get('college')
    Class = request.GET.get('Class')
    borrowNum = request.GET.get('borrowNum')
    allowNum = request.GET.get('allowNum')
    if students.objects.filter(studentId=studentId).first():
        print('该学号已存在')
        a = HttpResponse('该学号已存在，请重新填写')

        a['Access-Control-Allow-Origin'] = "http://localhost:8000"

        # 允许你携带Content-Type请求头
        a['Access-Control-Allow-Headers'] = "*"
        return a
    else:
        print('添加成功')
        student = students.objects.create(studentId=studentId, password=password, name=name, gender=gender,
                                          college=college, Class=Class, borrowNum=borrowNum, allowNum=allowNum)
        student.save()
        a = HttpResponse('添加成功')

        a['Access-Control-Allow-Origin'] = "http://localhost:8000"

        # 允许你携带Content-Type请求头
        a['Access-Control-Allow-Headers'] = "*"
        return a


# 返回查询学生页面
def inqstudent(request):
    return render(request, 'manager/inq_student.html')


# 判断学号是否存在
def isStudent(request):
    studentId = request.GET.get('studentId')
    student = students.objects.filter(studentId=studentId).first()
    print(student)
    if student:
        a = HttpResponse('ok'.encode('utf8'))

        a['Access-Control-Allow-Origin'] = "http://localhost:8000"

        # 允许你携带Content-Type请求头
        a['Access-Control-Allow-Headers'] = "*"
        return a
    else:
        a = HttpResponse('该学号不存在'.encode('utf8'))

        a['Access-Control-Allow-Origin'] = "http://localhost:8000"

        # 允许你携带Content-Type请求头
        a['Access-Control-Allow-Headers'] = "*"
        return a


# 返回查询的学生信息
def student(request):
    studentId = request.GET.get('studentId')
    student = students.objects.filter(studentId=studentId).first()
    return render(request, 'manager/student.html', {'student': student})


# 返回修改学生页面
def editstudent(request):
    return render(request, 'manager/edit_student.html')


# 返回修改的学生信息
def editstudents(request):
    studentId = request.GET.get('studentId')
    student = students.objects.filter(studentId=studentId).first()
    return render(request, 'manager/edit_students.html', {'student': student})


# 确定修改学生信息
def editStudent(request):
    Id = request.GET.get('Id')
    print(Id)
    studentId = request.GET.get('studentId')
    password = request.GET.get('password')
    name = request.GET.get('name1')
    gender = request.GET.get('gender')
    college = request.GET.get('college')
    Class = request.GET.get('Class')
    borrowNum = request.GET.get('borrowNum')
    allowNum = request.GET.get('allowNum')
    # print(studentId)
    student = students.objects.get(id=Id)
    student.studentId = studentId
    student.password = password
    student.name = name
    student.gender = gender
    student.college = college
    student.Class = Class
    student.borrowNum = borrowNum
    student.allowNum = allowNum
    student.save()
    return HttpResponse('修改成功'.encode('utf8'))


# 返回删除学生页面
def delstudent(request):
    return render(request, 'manager/del_student.html')


# 返回需要删除学生信息
def delstudents(request):
    studentId = request.GET.get('studentId')
    student = students.objects.filter(studentId=studentId).first()
    return render(request, 'manager/del_students.html', {'student': student})


# 确定是否删除
def isdelstudent(request):
    studentId = request.GET.get('studentId')
    print(studentId)
    students.objects.filter(studentId=studentId).delete()
    return HttpResponse('删除成功')


# 返回添加管理员页面
def addmanager(request):
    manager = request.session.get('manager')
    if manager == '超级管理员':
        return render(request, 'manager/add_manager.html')
    else:
        return HttpResponse('你不是超级管理员，权限不足')


# 确定添加管理员
def isaddmanager(request):
    name = request.GET.get('name1')
    account = request.GET.get('account')
    password = request.GET.get('password')
    manager = '普通管理员'
    managers.objects.create(name=name, account=account,
                            password=password, manager=manager)
    return HttpResponse('添加成功')


# 返回删除管理员页面
def delmanager(request):
    manager1 = request.session.get('manager')
    if manager1 == '超级管理员':
        manager = managers.objects.filter(manager='普通管理员')
        return render(request, 'manager/del_manager.html', {'manager': manager})
    else:
        return HttpResponse('你不是超级管理员，权限不足')


# 确定删除管理员
def isdelmanager(request):
    id = request.GET.get('id')
    managers.objects.filter(id=id).delete()
    return HttpResponse('删除成功')


# 注销
def logout(request):
    request.session.clear()
    return redirect('../../login/admin')


# 还书
def returnBook(request):
    if request.method == 'POST':
        studentId = request.POST.get('studentId')
        student = students.objects.filter(studentId=studentId).first()
        borrowList = borrowForm.objects.filter(student_id=student.id)
        bookList = []
        for borrow in borrowList:
            book = books.objects.filter(id=borrow.book_id).first()
            book1 = {
                "student": student.name,
                "studentId": studentId,
                "id": borrow.id,
                "number": book.number,
                "name": book.name,
                "author": book.author,
                "borrowTime": borrow.borrowTime.strftime("%Y-%m-%d %H:%M:%S"),
            }
            bookList.append(book1)
        return render(request, 'manager/return_book.html', {'bookList': bookList})
    return render(request, 'manager/return_book.html')


# 确认还书
def ReturnBook(request):
    Id = request.GET.get('id')
    book = borrowForm.objects.filter(id=Id).first()
    returnTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(returnTime)
    returnForm.objects.create(returnTime=returnTime, borrowTime=book.borrowTime,
                              book_id=book.book_id, student_id=book.student_id)
    borrowForm.objects.get(id=Id).delete()
    student1 = students.objects.get(id=book.student_id)
    student1.allowNum = student1.allowNum+1
    student1.borrowNum = student1.borrowNum-1
    student1.save()
    book1 = books.objects.get(id=book.book_id)
    book1.stock = book1.stock+1
    book1.save()
    return HttpResponse('还书成功')


# 借书
def borrowBook(request):
    return render(request, 'manager/borrow_book.html')


# 确认借书
def isborrowBook(request):
    studentId = request.GET.get('studentId')
    number = request.GET.get('number')
    student = students.objects.filter(studentId=studentId).first()
    book = books.objects.filter(number=number).first()
    borrowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    book1 = borrowForm.objects.filter(
        student_id=student.id, book_id=book.id).first()
    if book1:
        return HttpResponse('该书你已借')
    else:
        if student.allowNum != 0:
            book2 = books.objects.get(id=book.id)
            if book2.stock != 0:
                borrowForm.objects.create(borrowTime=borrowTime,
                                          student_id=student.id, book_id=book.id)
                student1 = students.objects.get(id=student_id)
                student1.allowNum = student1.allowNum-1
                student1.borrowNum = student1.borrowNum+1
                student1.save()
                book2.borrowedNum = book2.borrowedNum+1
                book2.stock = book2.stock-1
                book2.save()
                return HttpResponse('借书成功')
            else:
                return HttpResponse('库存不足')
        else:
            return HttpResponse('你的可借阅次数不足')
