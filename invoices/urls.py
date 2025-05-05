from django.urls import path
from .views import (
    APInvoiceListView,
    APInvoiceCreateView,
    DocumentHeaderListView
)

urlpatterns = [
    # APInvoice endpoints
    path('list/', APInvoiceListView.as_view(), name='ap-invoice-list'),
    path('create/', APInvoiceCreateView.as_view(), name='ap-invoice-create'),
    path('document-header/', DocumentHeaderListView.as_view(), name='document-header-list'),
]
