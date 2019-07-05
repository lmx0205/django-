from django.db import models

# Create your models here.


class students(models.Model):
    studentId = models.CharField(max_length=15, verbose_name='学号')
    password = models.CharField(max_length=15, verbose_name='密码')
    name = models.CharField(max_length=20, verbose_name='姓名')
    gender = models.CharField(max_length=2, verbose_name='姓别')
    college = models.CharField(max_length=20, verbose_name='学院')
    Class = models.CharField(max_length=40, verbose_name='班级')
    borrowNum = models.IntegerField(default=0, verbose_name='在借册数')
    allowNum = models.IntegerField(default=0, verbose_name='可借阅次数')
