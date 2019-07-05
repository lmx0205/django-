from django.db import models
from datetime import datetime

# Create your models here.


class managers(models.Model):
    name = models.CharField(max_length=20, verbose_name='管理员名字')
    manager = models.CharField(max_length=20, verbose_name='管理员类型')
    account = models.CharField(max_length=15, verbose_name='管理员账号')
    password = models.CharField(max_length=15, verbose_name='管理员密码')


class booktype(models.Model):
    style = models.CharField(max_length=15, verbose_name='书籍类型')


class books(models.Model):
    number = models.CharField(max_length=15, verbose_name='图书编号')
    name = models.CharField(max_length=20, null=True, verbose_name='书名')
    author = models.CharField(max_length=10, null=True, verbose_name='作者')
    style = models.ForeignKey(
        booktype, null=True, blank=True, on_delete=models.CASCADE, verbose_name='类型')
    price = models.IntegerField(default=0, verbose_name='价格')
    press = models.CharField(max_length=40, verbose_name='出版社')
    place = models.CharField(max_length=80, verbose_name='存放位置')
    borrowedNum = models.IntegerField(default=0, verbose_name='被借次数')
    stock = models.IntegerField(default=0, verbose_name='库存')
