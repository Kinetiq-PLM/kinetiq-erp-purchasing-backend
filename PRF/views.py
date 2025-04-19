from .models import PurchaseRequest
from .serializers import PurchaseRequestSerializer
from rest_framework import generics
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer

#Employee List View (GET all employees)
class EmployeeListView(generics.ListAPIView):  # ListAPIView for GET request
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# List view to get all purchase requests
class PurchaseRequestListView(generics.ListAPIView):  # Use ListAPIView for GET request
    queryset = PurchaseRequest.objects.all()  # Filter for requests without approval
    serializer_class = PurchaseRequestSerializer

# Submit view to create a new purchase request
class PurchaseRequestSubmitView(generics.CreateAPIView):  # Use CreateAPIView for POST request
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer

class PurchaseRequestPendingApprovalListView(generics.ListAPIView):  # Use ListAPIView for GET request
    """Retrieve a list of purchase requests without approval"""
    queryset = PurchaseRequest.objects.filter(approval_id__isnull=True).order_by('document_date')  # Filter for requests without approval
    serializer_class = PurchaseRequestSerializer