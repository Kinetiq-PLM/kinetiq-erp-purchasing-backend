# Create your views here.

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_data(request):
    data = {"message": "Hello from Django!"}
    return Response(data)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs): #DRF and ModelViewSet calls this method automatically
        """Handles stock updates and applies business rules"""
        item = self.get_object()
        order_qty = request.data.get("quantity", None)

        if order_qty is None:
            return Response({"error": "Quantity is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item.reduce_stock(int(order_qty))       #calls method from models.py
            return Response({"message": f"Stock updated! Remaining: {item.quantity}"})
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)