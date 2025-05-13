from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PurchaseRequest, Employee, Department
from .serializers import PurchaseRequestSerializer, EmployeeSerializer, DepartmentSerializer

class PurchaseRequestUpdateStatusView(generics.UpdateAPIView):
    """
    View to update the status of a PurchaseRequest.
    """
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer
    lookup_field = 'request_id'  # Use 'request_id' as the lookup field

    def partial_update(self, request, *args, **kwargs):
        """
        Handle PATCH requests to update only the status field.
        """
        instance = self.get_object()
        status = request.data.get('status', None)
        if status:
            instance.status = status
            instance.save()
            return Response({'message': f'Status updated to {status}'}, status=http_status.HTTP_200_OK)
        return Response({'error': 'Status not provided'}, status=http_status.HTTP_400_BAD_REQUEST)

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

class DepartmentListView(generics.ListAPIView):
    """
    View to retrieve a list of all departments.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer