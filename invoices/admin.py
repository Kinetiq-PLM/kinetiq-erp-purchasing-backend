from django.contrib import admin
from .models import APInvoice  # Ensure APInvoice is imported

class APInvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_id", "get_purchase_id", "status", "document_no")

    def get_purchase_id(self, obj):
        return obj.purchase_order.purchase_id if obj.purchase_order else "N/A"

    get_purchase_id.short_description = "Purchase Order ID"  # Sets column name in admin panel

admin.site.register(APInvoice, APInvoiceAdmin)
