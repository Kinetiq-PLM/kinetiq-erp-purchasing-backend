from rest_framework.generics import ListAPIView
from .models import CreditMemo
from .serializers import CreditMemoSerializer

class CreditMemoListView(ListAPIView):
    queryset = CreditMemo.objects.all()
    serializer_class = CreditMemoSerializer
