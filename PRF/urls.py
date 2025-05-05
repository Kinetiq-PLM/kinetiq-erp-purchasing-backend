from django.urls import path
from .views import PurchaseRequestListView, PurchaseRequestSubmitView,PurchaseRequestUpdateStatusView
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('submit/', PurchaseRequestSubmitView.as_view(), name='purchase_request_submit'),
    path('list/', PurchaseRequestListView.as_view(), name='purchase_request_list'),
    path('update/<str:request_id>/', PurchaseRequestUpdateStatusView.as_view(), name='purchase_request_update_status'),
]
