from django.contrib import admin
from .models import PurchaseRequest, Employee, Approval

class PurchaseRequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'employee_id', 'approval_id', 'valid_date', 'document_date', 'required_date',  ]
  
    search_fields = ['request_id', 'employee_id__first_name', 'employee_id__last_name', 'approval_id__approval_id']

    fieldsets = (
        (None, {
            'fields': ('request_id', 'employee_id', 'approval_id', 'valid_date', 'document_date', 'required_date',)
        }),
    )

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'dept_id')  # Custom fields for display
    search_fields = ('employee_id', 'first_name', 'last_name')  # Enable search

  



# Register models with their custom admin views
admin.site.register(PurchaseRequest, PurchaseRequestAdmin)
admin.site.register(Employee, EmployeeAdmin)  # Make sure you're registering Employee with the custom admin
admin.site.register(Approval)
