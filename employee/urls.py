from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add-employee/', EmployeeAPIView.as_view(), name='employee-add'),
    path('get-departments/', get_employee_departments, name='get-departs'),  
    path('get-employees/', EmployeeAPIView.as_view(), name='employee-list'), 
    path('get-employee/<str:employee_id>/',get_employee,name='get-employee-id'),
    path('update-employee/<str:employee_id>/', update_employee, name='employee-update'), 
    path('delete-employee/<str:employee_id>/', delete_employee, name='employee-delete'),  
]