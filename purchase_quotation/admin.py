from django.contrib import admin
from .models import PurchaseQuotation, Vendor

class PurchaseQuotationAdmin(admin.ModelAdmin):
    list_display = (
        'quotation_id', 
        'get_vendor_code', 
        'document_no', 
        'status',  # <- use field name from model, not DB column name
        'valid_date', 
        'document_date', 
        'required_date', 
        'total_payment',
        'remarks',
        'delivery_loc',
        'downpayment_request',
        
    )
    search_fields = ('quotation_id', 'vendor_code__vendor_code', 'document_no')
    list_filter = ('status', 'valid_date', 'document_date', 'required_date')

    def get_vendor_code(self, obj):
        return obj.vendor_code.vendor_code
    get_vendor_code.short_description = 'Vendor Code'

class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_code','company_name', 'contact_person')
    search_fields = ('vendor_code',)

admin.site.register(PurchaseQuotation, PurchaseQuotationAdmin)
admin.site.register(Vendor, VendorAdmin)
