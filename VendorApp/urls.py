from django.urls import path
from .views import VendorApplicationListView, VendorApplicationCreateView, VendorApplicationUpdateStatusView

urlpatterns = [
    path("list/", VendorApplicationListView.as_view(), name="vendor-app-list"),
    path("create/", VendorApplicationCreateView.as_view(), name="vendor-app-create"),
    path('edit/<str:vendor_code>/', VendorApplicationUpdateStatusView.as_view(), name='vendor-application-update-status'),
]
