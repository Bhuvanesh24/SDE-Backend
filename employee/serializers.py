from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    # Explicitly provide the available choices for the frontend
    department_choices = serializers.SerializerMethodField()

    def get_department_choices(self, obj):
        return Employee.DEPARTMENT_CHOICES

    def validate_email(self, value):
        """
        Validate that the email is unique.
        """
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("An employee with this email already exists.")
        return value
    
    def validate_phone_number(self, value):
        """
        Validate that the phone number is unique and format is correct.
        """
        # Call the validation function
        
        
        # Check for uniqueness
        if Employee.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("An employee with this phone number already exists.")
        
        return value
    
    def validate_employee_id(self,value):
        if Employee.objects.filter(employee_id=value).exists():
            raise serializers.ValidationError("An employee with this employee id already exists.")
        return value

    # def validate_phone_number(self, value):
    #     """
    #     Validate phone number format (should be 10 digits).
    #     """
    #     if len(value) != 10 or not value.isdigit():
    #         raise serializers.ValidationError("Phone number must be a 10-digit number.")
    #     return value
