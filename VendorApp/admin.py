from django.contrib import admin
from .models import VendorApplication

class VendorApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_reference', 'company_name', 'status', 'requestor', 'date_requested')
    list_filter = ('status', 'date_requested')
    search_fields = ('application_reference', 'company_name', 'requestor')
    ordering = ('-date_requested',)

    # You can also define fieldsets to control how the form appears when creating/editing the model
    fieldsets = (
        (None, {
            'fields': ('application_reference', 'company_name', 'tax_number', 'contact_person', 'title', 'vendor_address', 'phone', 'fax', 'vendor_email')
        }),
        ('Financial Information', {
            'fields': ('tax_exempt', 'vendor_website', 'organization_type', 'separate_checks', 'purchasing_card', 'account_no', 'routing_no')
        }),
        ('Request Information', {
            'fields': ('requestor', 'date_requested', 'status')
        }),
    )

    # Optionally, add readonly fields
    readonly_fields = ('application_reference',)

admin.site.register(VendorApplication, VendorApplicationAdmin)
