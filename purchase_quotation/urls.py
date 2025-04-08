from django.urls import path
from .views import PurchaseQuotationListView, PurchaseQuotationCreateView, VendorListView, PurchaseQuotationDocumentNoListView, PurchaseQuotationEditView

urlpatterns = [
    path('list/', PurchaseQuotationListView.as_view(), name='purchase-quotation-list'),
    path('create/', PurchaseQuotationCreateView.as_view(), name='purchase-quotation-create'),
    path('vendor/list/', VendorListView.as_view(), name='vendor-list'),  # Assuming you have a VendorListView
    path('edit/<str:quotation_id>/', PurchaseQuotationEditView.as_view(), name='purchase-quotation-edit'),
    path('document/list/', PurchaseQuotationDocumentNoListView.as_view(), name='quotation-by-document-no'),
]