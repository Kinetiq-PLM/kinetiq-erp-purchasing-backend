from rest_framework import serializers
from .models import QuotationContent, RawMaterials, Assets, PurchaseRequest
from PRF.serializers import PurchaseRequestSerializer  # Importing the PurchaseRequestSerializer from prf app

class RawMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterials
        fields = ['material_id', 'material_name', 'cost_per_unit']

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ['asset_id', 'asset_name', 'purchase_price']

class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = ['request_id']

class QuotationContentSerializer(serializers.ModelSerializer):
    material = RawMaterialsSerializer(read_only=True)
    asset = AssetsSerializer(read_only=True)
    request = PurchaseRequestSerializer(read_only=True)

    class Meta:
        model = QuotationContent
        fields = [

            'unit_price', 
            'discount', 
            'tax_code', 
            'total', 
            'material_id', 
            'asset_id', 
            'request_id', 
            'purchase_quantity',
            'material',
            'asset',
            'request'
        ]

    def validate(self, data):
        # Custom validation if needed
        if not data.get('material_id') and not data.get('asset_id'):
            raise serializers.ValidationError("Either material_id or asset_id must be provided.")
        # Ensure unit_price and purchase_quantity are provided
        if not data.get('purchase_quantity'):
            raise serializers.ValidationError("purchase_quantity is required.")
        
        return data
def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Adding material and asset prices to the response
        if instance.material:
            representation['material_price'] = instance.material.cost_per_unit
        if instance.asset:
            representation['asset_price'] = instance.asset.purchase_price
        
        return representation
