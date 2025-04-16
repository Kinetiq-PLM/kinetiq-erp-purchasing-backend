from django.urls import path
from .views import ShipmentCreateView, ShipmentListView

urlpatterns = [
    path('create/', ShipmentCreateView.as_view(), name='shipment-create'),
    path('list/', ShipmentListView.as_view(), name='shipment-list'),
]