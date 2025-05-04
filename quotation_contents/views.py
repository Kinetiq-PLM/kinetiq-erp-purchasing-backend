from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import QuotationContent, RawMaterials
from .serializers import QuotationContentSerializer, RawMaterialsSerializer


class CheckQuotationContentView(APIView):
    def get(self, request, request_id):
        exists = QuotationContent.objects.filter(request_id=request_id).exists()
        return Response({"exists": exists}, status=status.HTTP_200_OK)

# List view to get all raw materials
class RawMaterialsListView(generics.ListAPIView):
    queryset = RawMaterials.objects.all()
    serializer_class = RawMaterialsSerializer

# List view to get all quotation contents
class QuotationContentListView(generics.ListAPIView):
    queryset = QuotationContent.objects.all()
    serializer_class = QuotationContentSerializer

# Create view to add a new quotation content
class QuotationContentCreateView(generics.CreateAPIView):
    queryset = QuotationContent.objects.all()
    serializer_class = QuotationContentSerializer

# Update view to modify discount, unit_price, and total
class QuotationContentUpdateView(generics.UpdateAPIView):
    """
    View to update discount, unit_price, and total for a QuotationContent.
    """
    queryset = QuotationContent.objects.all()
    serializer_class = QuotationContentSerializer
    lookup_field = 'quotation_content_id'  # Use quotation_content_id as the lookup field

    def partial_update(self, request, *args, **kwargs):
        """
        Handle PATCH requests to update specific fields.
        """
        instance = self.get_object()
        discount = request.data.get('discount', None)
        unit_price = request.data.get('unit_price', None)

        # Update discount and unit_price even if they are null
        if discount is not None:
            instance.discount = discount
        if unit_price is not None:
            instance.unit_price = unit_price

        # Recalculate total even if unit_price or purchase_quantity is null
        if instance.unit_price is not None and instance.purchase_quantity is not None:
            total = instance.unit_price * instance.purchase_quantity
            if instance.discount:
                total -= total * (instance.discount / 100)
            instance.total = round(total, 2)
        else:
            instance.total = None  # Set total to None if calculation is not possible

        instance.save()
        return Response(
            {
                "message": "QuotationContent updated successfully",
                "quotation_content_id": instance.quotation_content_id,
                "unit_price": instance.unit_price,
                "discount": instance.discount,
                "total": instance.total,
            },
            status=status.HTTP_200_OK
        )