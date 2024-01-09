from django.db import models

# Create your models here.
class Department(models.Model):
    depname=models.CharField(max_length=200)
    depcode=models.CharField(max_length=200)
    status=models.IntegerField(default=1)

class Designation(models.Model):
    desname=models.CharField(max_length=20)
    descode=models.CharField(max_length=10)
    status=models.IntegerField(default=1)

class Qualification(models.Model):
    qualname=models.CharField(max_length=200)
    status=models.IntegerField(default=1)

class Class(models.Model):
    classname=models.CharField(max_length=20)
    status=models.IntegerField(default=1)

class Division(models.Model):
    divname=models.CharField(max_length=20)
    status=models.IntegerField(default=1)

class Employee_category(models.Model):
    employee_category_choices=[
        (1,'Accountant'),
        (2,'Cafeteria'),
        (3,'Librarian'),
        (4,'Teacher'),
        (5,'Other'),
    ] 
    ename=models.CharField(max_length=200)
    area=models.IntegerField(choices=employee_category_choices)
    status=models.IntegerField(default=1)

class Subject(models.Model):
    sname=models.CharField(max_length=200)
    status=models.IntegerField(default=1)

class Subject_class(models.Model):
    classid=models.ForeignKey(Class,on_delete=models.CASCADE)
    subid=models.ForeignKey(Subject,on_delete=models.CASCADE)
    