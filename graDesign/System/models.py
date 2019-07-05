from django.db import models
from Login.models import students
from Manager.models import books
# Create your models here.


class borrowForm(models.Model):
    book = models.ForeignKey(
        books, null=True, blank=True, on_delete=models.CASCADE, verbose_name='图书')
    student = models.ForeignKey(
        students, null=True, blank=True, on_delete=models.CASCADE, verbose_name='学生')
    borrowTime = models.DateTimeField(verbose_name='借书时间', auto_now_add=True)


class returnForm(models.Model):
    book = models.ForeignKey(
        books, null=True, blank=True, on_delete=models.CASCADE, verbose_name='图书')
    student = models.ForeignKey(
        students, null=True, blank=True, on_delete=models.CASCADE, verbose_name='学生')
    borrowTime = models.DateTimeField(
        verbose_name='借书时间', auto_now_add=False, null=True)
    returnTime = models.DateTimeField(
        verbose_name='还书时间', auto_now_add=True, null=True)
