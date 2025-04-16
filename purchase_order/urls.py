from django.urls import path
from .views import PurchaseOrderListCreateView,PurchaseOrderUpdateStatusView,PurchaseOrderEditView

urlpatterns = [
    path('orders/<str:purchase_id>/update-status/', PurchaseOrderUpdateStatusView.as_view(), name='purchase-order-update-status'),
    path('list/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
     path('edit/<str:purchase_id>/', PurchaseOrderEditView.as_view(), name='purchase_order_edit'),
]
