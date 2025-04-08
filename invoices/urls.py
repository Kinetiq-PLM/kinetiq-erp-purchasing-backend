from django.urls import path
from .views import APInvoiceListView

urlpatterns = [
    path("list/", APInvoiceListView.as_view(), name="api-invoices"),
]
