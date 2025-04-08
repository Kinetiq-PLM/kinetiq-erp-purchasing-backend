from django.contrib import admin
from .models import PurchaseOrder

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('purchase_id', 'quotation_id', 'order_date', 'delivery_date', 'document_date', 'status')
    search_fields = ('purchase_id', 'quotation_id', 'status')
    list_filter = ('status', 'order_date')

