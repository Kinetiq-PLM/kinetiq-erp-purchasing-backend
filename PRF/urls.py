from django.urls import path
from .views import PurchaseRequestListView, PurchaseRequestSubmitView, PurchaseRequestPendingApprovalListView
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('submit/', PurchaseRequestSubmitView.as_view(), name='purchase_request_submit'),
    path('list/', PurchaseRequestListView.as_view(), name='purchase_request_list'),
    path('null/', PurchaseRequestPendingApprovalListView.as_view(), name='purchase_request_pending_approval')
]
