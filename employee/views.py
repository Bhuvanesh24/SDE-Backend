from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view


class EmployeeAPIView(APIView):
    
    def get(self, request):
        """
        Fetch all employees.
        """
        employees = Employee.objects.all()  # Fetch all employees
        serializer = EmployeeSerializer(employees, many=True)  # Serialize employees
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST request to add a new employee.
        """
        
        serializer = EmployeeSerializer(data=request.data)
        
        # Check if the serializer is valid
        if serializer.is_valid():
            try:
                # Try to save the new employee
                serializer.save()
                return Response({"message": "Employee added successfully!"}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                # Handle unique constraints (employee_id, email)
                if "employee_id" in str(e):
                    return Response({"error": "Employee ID already exists."}, status=status.HTTP_400_BAD_REQUEST)
                if "email" in str(e):
                    return Response({"error": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)
                if "phone_number" in str(e):
                    return Response({"error": "Phone number already exists."}, status=status.HTTP_400_BAD_REQUEST)
        # If validation fails, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def get_employee_departments(request):
    """
    Returns the list of available department choices as JSON.
    """
    # Fetch department choices from the model
    departments = [{"value": choice[0], "label": choice[1]} for choice in Employee.DEPARTMENT_CHOICES]
    return JsonResponse({"departments": departments})



@api_view(['PUT'])
def update_employee(request, employee_id):
    """
    Handle PUT request to update an existing employee.
    """
    print(request.data)
    try:
        employee = Employee.objects.get(employee_id=employee_id) 
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = EmployeeSerializer(employee, data=request.data, partial=True) 

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Employee updated successfully!"}, status=status.HTTP_200_OK)
    print("Validation Errors:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_employee(request, employee_id):
    """
    Handle DELETE request to delete an employee.
    """
    try:
        employee = Employee.objects.get(employee_id=employee_id)  # Find employee by ID
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)

    employee.delete()  # Delete the employee
    return Response({"message": "Employee deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_employee(request, employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)  # Find employee by ID
    
    except Employee.DoesNotExist:

        return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(employee)  # Serialize the employee
    return Response(serializer.data, status=status.HTTP_200_OK)
