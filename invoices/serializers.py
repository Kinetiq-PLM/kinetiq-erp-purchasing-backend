from rest_framework import serializers
from .models import APInvoice, DocumentHeader # Ensure ExternalModule and DocumentItems are imported


class APInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = APInvoice
        fields = "__all__"  # Include all fields from the APInvoice model


class DocumentHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentHeader
        fields = "__all__"  # Include all fields from the DocumentItems model