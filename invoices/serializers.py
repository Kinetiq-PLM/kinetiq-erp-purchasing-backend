from rest_framework import serializers
from .models import APInvoice, ExternalModule, DocumentItems  # Ensure ExternalModule and DocumentItems are imported


class APInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = APInvoice
        fields = "__all__"  # Include all fields from the APInvoice model


class ExternalModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalModule
        fields = "__all__"  # Include all fields from the ExternalModule model


class DocumentItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentItems
        fields = "__all__"  # Include all fields from the DocumentItems model