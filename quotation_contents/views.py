from rest_framework import generics
from .models import QuotationContent, RawMaterials, Assets, PurchaseRequest
from .serializers import QuotationContentSerializer, RawMaterialsSerializer, AssetsSerializer, PurchaseRequestSerializer

# List view to get all raw materials
class RawMaterialsListView(generics.ListAPIView):
    queryset = RawMaterials.objects.all()
    serializer_class = RawMaterialsSerializer

# List view to get all assets
class AssetsListView(generics.ListAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

# List view to get all quotation contents
class QuotationContentListView(generics.ListAPIView):
    queryset = QuotationContent.objects.all()
    serializer_class = QuotationContentSerializer

# Create view to add a new quotation content
class QuotationContentCreateView(generics.CreateAPIView):
    queryset = QuotationContent.objects.all()
    serializer_class = QuotationContentSerializer
