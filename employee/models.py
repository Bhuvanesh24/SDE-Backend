from django.db import models
from django.db.models.signals import post_save




class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('Engineering', 'Engineering'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
    ]

    employee_id = models.CharField(max_length=15, unique=True)  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=25,blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(max_length=13,unique=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    date_of_joining = models.DateField()
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

