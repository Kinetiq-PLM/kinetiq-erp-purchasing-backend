from rest_framework import serializers
from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = [

            'purchase_id', 
            'quotation_id', 
            'order_date', 
            'delivery_date', 
            'document_date', 
            'status'
        ]
        extra_kwargs = {
            'quotation_id': {'required': False, 'allow_null': True},  # Make quotation_id optional
        }



# serializers.py is specific to Django REST Framework (DRF), 
# which is an optional package for building APIs.

# serializers.ModelSerializer → Automatically converts Django model instances into JSON format (and vice versa).
# class Meta: → Provides metadata about the serializer, specifying:
# model = Item → The model being serialized.
# fields = '__all__' → Includes all fields of the Item model in the serialized output.