from rest_framework import generics, status as http_status
from rest_framework.response import Response
from .models import VendorApplication
from .serializers import VendorApplicationSerializer

class VendorApplicationListView(generics.ListAPIView):
    """Retrieve a list of all vendor applications"""
    queryset = VendorApplication.objects.all()
    serializer_class = VendorApplicationSerializer

class VendorApplicationCreateView(generics.CreateAPIView):
    """Create a new vendor application"""
    queryset = VendorApplication.objects.all()
    serializer_class = VendorApplicationSerializer

class VendorApplicationUpdateStatusView(generics.UpdateAPIView):
    """
    View to update the status of a VendorApplication.
    """
    queryset = VendorApplication.objects.all()
    serializer_class = VendorApplicationSerializer
    lookup_field = 'vendor_code'  

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