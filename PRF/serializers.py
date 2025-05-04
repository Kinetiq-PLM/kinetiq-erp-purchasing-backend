from rest_framework import serializers
from .models import PurchaseRequest
from .models import Employee

# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # Include all fields from the Employee model

# PurchaseRequest Serializer
class PurchaseRequestSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)  # Include nested employee details (optional)

    class Meta:
        model = PurchaseRequest
        fields = '__all__'  # Automatically include all fields from the PurchaseRequest model

    def validate(self, data):
        if not data.get('employee_id'):
            raise serializers.ValidationError("Employee ID is required.")
        return data