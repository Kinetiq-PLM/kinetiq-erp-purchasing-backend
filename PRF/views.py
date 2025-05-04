from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PurchaseRequest, Employee
from .serializers import PurchaseRequestSerializer, EmployeeSerializer

class EmployeeListView(generics.ListAPIView):
    """
    View to retrieve a list of all employees.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PurchaseRequestListView(generics.ListAPIView):
    """
    View to retrieve a list of all purchase requests.
    """
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer

class PurchaseRequestSubmitView(generics.CreateAPIView):
    """
    View to create a new purchase request.
    """
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer