from rest_framework import serializers
from .models import PurchaseQuotation
from purchase_quotation.models import Vendor # Import the related models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_code', 'vendor_name', 'contact_person']



class PurchaseQuotationSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = PurchaseQuotation
        read_only_fields = ['quotation_id']
        fields = "__all__"  
        fields = [
            'quotation_id',
            'vendor',
            'vendor_code',
            'document_no',
            'status',
            'valid_date',
            'document_date',
            'required_date',
            'total_before_discount',
            'discount_percent',
            'freight',
            'tax',
            'total_payment',
            'request_id',
            'remarks',
            'delivery_loc',
            'downpayment_request',
        ]

