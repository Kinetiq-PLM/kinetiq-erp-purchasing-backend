from rest_framework import serializers
from .models import CreditMemo

class CreditMemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditMemo
        fields = "__all__"  # Include all fields





# serializers.py is specific to Django REST Framework (DRF), 
# which is an optional package for building APIs.

# serializers.ModelSerializer → Automatically converts Django model instances into JSON format (and vice versa).
# class Meta: → Provides metadata about the serializer, specifying:
# model = Item → The model being serialized.
# fields = '__all__' → Includes all fields of the Item model in the serialized output.