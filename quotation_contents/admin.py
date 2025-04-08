from django.contrib import admin
from .models import RawMaterials, Assets, QuotationContent

# Admin configuration for RawMaterials
@admin.register(RawMaterials)
class RawMaterialsAdmin(admin.ModelAdmin):
    list_display = ('material_id', 'material_name','cost_per_unit')
    search_fields = ('material_id', 'material_name')

# Admin configuration for Assets
@admin.register(Assets)
class AssetsAdmin(admin.ModelAdmin):
    list_display = ('asset_id', 'asset_name', 'purchase_price')
    search_fields = ('asset_id', 'asset_name')

# Admin configuration for QuotationContent
@admin.register(QuotationContent)
class QuotationContentAdmin(admin.ModelAdmin):
    readonly_fields = ('quotation_content_id',)
    fields = ('quotation_content_id', 'request_id', 'unit_price', 'discount', 'tax_code', 'total', 'material_id', 'asset_id', 'purchase_quantity')
    
    