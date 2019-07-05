from django.shortcuts import render, redirect, HttpResponse
from .models import borrowForm, returnForm
from Manager.models import books, booktype
from Login.models import students
from django.db.models import Q
import datetime

# Create your views here.


# 返回图书馆首页
def index(request):
    return render(request, 'system/index.html')


# 返回查询图书页面
def query(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        print(keyword)
        bookList = books.objects.filter(
            Q(name__icontains=keyword) | Q(author__icontains=keyword))
        # print(bookList)
        return render(request, 'system/query.html', {'bookList': bookList})
    return render(request, 'system/query.html')


# 借书确认
def borrowbook(request):
    student_id = request.session.get('id')
    book_id = request.GET.get('id')
    student = students.objects.filter(id=student_id).first()
    borrowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(borrowTime)
    print('可借阅次数', student.allowNum)
    print(student_id)
    print(book_id)
    book = borrowForm.objects.filter(
        student_id=student_id, book_id=book_id).first()
    if book:
        return HttpResponse('该书你已借')
    else:
        if student.allowNum != 0:
            book1 = books.objects.get(id=book_id)
            if book1.stock != 0:
                borrowForm.objects.create(borrowTime=borrowTime,
                                          student_id=student_id, book_id=book_id)
                student1 = students.objects.get(id=student_id)
                student1.allowNum = student1.allowNum-1
                student1.borrowNum = student1.borrowNum+1
                student1.save()
                book1.borrowedNum = book1.borrowedNum+1
                book1.stock = book1.stock-1
                book1.save()
                return HttpResponse('借书成功')
            else:
                return HttpResponse('库存不足')
        else:
            return HttpResponse('你的可借阅次数不足')


# 返回还书页面
def Return(request):
    student_id = request.session.get('id')
    borrowList = borrowForm.objects.filter(student_id=student_id)
    bookList = []
    for borrow in borrowList:
        book = books.objects.filter(id=borrow.book_id).first()
        book1 = {
            "id": borrow.id,
            "number": book.number,
            "name": book.name,
            "author": book.author,
            "borrowTime": borrow.borrowTime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        bookList.append(book1)
    # print(bookList)
    return render(request, 'system/return.html', {'bookList': bookList})


# 确认还书
def ReturnBook(request):
    Id = request.GET.get('id')
    print(Id)
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


#个人信息查看
def info(request):
    student_id = request.session.get('id')
    student = students.objects.filter(id=student_id).first()
    borrowList = borrowForm.objects.filter(student_id=student_id)
    bookList = []
    for borrow in borrowList:
        book = books.objects.filter(id=borrow.book_id).first()
        book1 = {
            "id": borrow.id,
            "number": book.number,
            "name": book.name,
            "author": book.author,
            "borrowTime": borrow.borrowTime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        bookList.append(book1)
    returnList = returnForm.objects.filter(
        student_id=student_id).order_by("-returnTime")
    RbookList = []
    for Return in returnList:
        book2 = books.objects.filter(id=Return.book_id).first()
        book3 = {
            "id": book2.id,
            "number": book2.number,
            "name": book2.name,
            "author": book2.author,
            "borrowTime": Return.borrowTime.strftime("%Y-%m-%d %H:%M:%S"),
            "returnTime": Return.returnTime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        RbookList.append(book3)
    return render(request, 'system/info.html', {'student': student, 'bookList': bookList, 'RbookList': RbookList})


def logout(request):
    request.session.clear()
    return redirect('../../login/login')
