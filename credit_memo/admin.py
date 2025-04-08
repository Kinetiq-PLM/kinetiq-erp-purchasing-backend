from django.contrib import admin
from .models import CreditMemo

@admin.register(CreditMemo)
class CreditMemoAdmin(admin.ModelAdmin):
    list_display = ("credit_memo_id", "status", "document_no", "total_credit")
    search_fields = ("credit_memo_id", "inspection__inspection_id")  # Ensure Inspection model has `inspection_id`
    list_filter = ("status", "document_date", "due_date")
