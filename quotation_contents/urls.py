from django.urls import path
from .views import QuotationContentListView, QuotationContentCreateView, RawMaterialsListView, AssetsListView

urlpatterns = [
    path('list/', QuotationContentListView.as_view(), name='quotation_content_list'),  # List view
    path('create/', QuotationContentCreateView.as_view(), name='quotation_content_create'),  # Create view
    path('materials/list/', RawMaterialsListView.as_view(), name='raw_materials_list'),
    path('assets/list/', AssetsListView.as_view(), name='assets_list'),
    
]
