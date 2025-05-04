from django.contrib import admin
from .models import RawMaterials,  QuotationContent

# Admin configuration for RawMaterials
@admin.register(RawMaterials)
class RawMaterialsAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'item_type')
    search_fields = ('item_id', 'item_name', 'item_type')



# Admin configuration for QuotationContent
@admin.register(QuotationContent)
class QuotationContentAdmin(admin.ModelAdmin):
    readonly_fields = ('quotation_content_id',)
    fields = ('quotation_content_id', 'request_id', 'unit_price', 'discount', 'tax_code', 'total', 'item_id', 'asset_id', 'purchase_quantity')
    
    