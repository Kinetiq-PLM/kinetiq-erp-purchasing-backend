from django.urls import path
from .views import (
    APInvoiceListView,
    APInvoiceCreateView,
    ExternalModuleListView,
    DocumentItemsListView,
)

urlpatterns = [
    # APInvoice endpoints
    path('list/', APInvoiceListView.as_view(), name='ap-invoice-list'),
    path('create/', APInvoiceCreateView.as_view(), name='ap-invoice-create'),

    # ExternalModule endpoints
    path('external-modules/', ExternalModuleListView.as_view(), name='external-module-list'),

    # DocumentItems endpoints
    path('document-items/', DocumentItemsListView.as_view(), name='document-items-list'),
]
