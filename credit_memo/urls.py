from django.urls import path
from .views import CreditMemoListView

urlpatterns = [
    path("list/", CreditMemoListView.as_view(), name="credit-memo-list"),
]