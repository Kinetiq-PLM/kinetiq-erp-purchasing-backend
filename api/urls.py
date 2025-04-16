# 'path' is used to define URL patterns, 'include' allows including other URL configurations
from django.urls import path, include  

# DRF's DefaultRouter automatically generates RESTful routes for ViewSets
from rest_framework.routers import DefaultRouter  

# Import the ItemViewSet, which will handle API requests for the Item model
from .views import ItemViewSet  

# Create a DRF router instance
router = DefaultRouter()  # DefaultRouter automatically sets up standard RESTful routes like list, create, retrieve, update, delete
router.register(r'items', ItemViewSet)  # Registers the 'ItemViewSet' under the 'items' route (e.g., /api/items/)
# When you change 'items' here, it directly affects the API endpoint URL.
from django.urls import path
from .views import get_data


# Define the URL patterns
urlpatterns = [
    path(' ', include(router.urls)),  # Includes all generated routes under the 'api/' prefix (e.g., /api/items/)
    path("data/", get_data),  # API endpoint
    path("invoices/", include("invoices.urls")),
    path("prf/", include("PRF.urls")),
    path('purchase_quotation/', include('purchase_quotation.urls')),
    path("VendorApp/", include("VendorApp.urls")),
    path('purchase-orders/', include('purchase_order.urls')),
    path("credit-memo/", include("credit_memo.urls")),
    path("quotation-content/", include("quotation_contents.urls")),
    path("batch-inspection/", include("batch_inspection.urls")),
    path("received-shipment/", include("received_shipments.urls")),

]