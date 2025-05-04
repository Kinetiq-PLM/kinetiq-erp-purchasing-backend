from django.urls import path
from .views import QuotationContentListView, QuotationContentCreateView, RawMaterialsListView, CheckQuotationContentView, QuotationContentUpdateView

urlpatterns = [
    path('list/', QuotationContentListView.as_view(), name='quotation_content_list'),  # List view
    path('create/', QuotationContentCreateView.as_view(), name='quotation_content_create'),  # Create view
    path('item/list/', RawMaterialsListView.as_view(), name='raw_materials_list'),
    path('check/<str:request_id>/', CheckQuotationContentView.as_view(), name="check-quotation-content"),
    path('update/<str:quotation_content_id>/', QuotationContentUpdateView.as_view(), name='quotation_content_update'),  # Update view
]
