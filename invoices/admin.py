from django.contrib import admin
from .models import DocumentItems, ExternalModule, APInvoice


@admin.register(DocumentItems)
class DocumentItemsAdmin(admin.ModelAdmin):
    list_display = ('content_id',)  # Display the content_id field in the admin list view


@admin.register(ExternalModule)
class ExternalModuleAdmin(admin.ModelAdmin):
    list_display = ('content_id', 'purchase_id', 'request_id')  # Display these fields in the admin list view


@admin.register(APInvoice)
class APInvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_id',
        'status',
        'document_no',
        'document_date',
        'due_date',
        'total_credit',
        'credit_balance',
        'dpm_rate',
        'dpm_amount',
        'applied_amount',
        'balance_due',
    )  # Display these fields in the admin list view
    list_filter = ('status', 'document_date', 'due_date')  # Add filters for these fields
    search_fields = ('invoice_id', 'document_no')  # Add search functionality for these fields