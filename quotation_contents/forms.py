from django import forms
from .models import QuotationContent

class QuotationContentForm(forms.ModelForm):
    class Meta:
        model = QuotationContent
        fields = ['quotation_content_id', 'unit_price', 'discount', 'tax_code', 'total', 'material_id', 'asset_id', 'purchase_quantity']
