from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    """
    Generic view to list all purchase orders or create a new one.
    """
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderUpdateStatusView(generics.UpdateAPIView):
    """
    View to update the status of a PurchaseOrder.
    """
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'purchase_id'  # Use purchase_id as the lookup field

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