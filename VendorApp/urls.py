from django.urls import path
from .views import VendorApplicationListView, VendorApplicationCreateView

urlpatterns = [
    path("list/", VendorApplicationListView.as_view(), name="vendor-app-list"),
    path("create/", VendorApplicationCreateView.as_view(), name="vendor-app-create"),
]
