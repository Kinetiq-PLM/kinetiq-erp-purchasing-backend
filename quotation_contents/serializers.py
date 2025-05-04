from rest_framework import serializers
from .models import QuotationContent, RawMaterials, PurchaseRequest
from PRF.serializers import PurchaseRequestSerializer  # Importing the PurchaseRequestSerializer from prf app

class RawMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterials
        fields = ['item_id', 'item_name', 'item_type']


class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = ['request_id']

class QuotationContentSerializer(serializers.ModelSerializer):
    material = RawMaterialsSerializer(read_only=True)
    request = PurchaseRequestSerializer(read_only=True)

    class Meta:
        model = QuotationContent
        fields = '__all__'
        read_only_fields = ['quotation_content_id'] 
      
