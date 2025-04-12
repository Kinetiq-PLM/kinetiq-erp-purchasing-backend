from rest_framework import serializers
from .models import PurchaseRequest
from purchase_quotation.models import PurchaseQuotation  # Assuming the app name for PurchaseQuotation is `quotation_quotation`
from .models import Employee, Approval

# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name', 'dept_id', 'employment_type', 'status']

# Approval Serializer
class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = ['approval_id']


# PurchaseRequest Serializer
class PurchaseRequestSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    approval = ApprovalSerializer(read_only=True)

    class Meta:
        model = PurchaseRequest
        fields = [
            'request_id',
            'employee_id',
            'approval_id',
            'approval',
            'valid_date',
            'document_date',
            'required_date',
            'employee'
        ]

    def validate(self, data):
        if not data.get('employee_id'):
            raise serializers.ValidationError("Employee ID is required.")
        return data
