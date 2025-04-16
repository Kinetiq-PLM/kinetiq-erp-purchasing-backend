from django.db import models
from batch_inspection.models import Inspection  # Ensure this import is correct

    

class CreditMemo(models.Model):
    credit_memo_id = models.CharField(primary_key=True, max_length=255)
    inspection = models.ForeignKey(
        Inspection,  # Use Inspection as the reference
        on_delete=models.CASCADE, 
        db_column="inspection_id"
    )
    status = models.CharField(max_length=255)
    document_no = models.IntegerField()
    document_date = models.DateField()
    delivery_date = models.DateField()
    due_date = models.DateField()
    total_credit = models.DecimalField(max_digits=10, decimal_places=2)
    credit_balance = models.DecimalField(max_digits=10, decimal_places=2)
    dpm_rate = models.DecimalField(max_digits=5, decimal_places=2)
    dpm_amount = models.DecimalField(max_digits=10, decimal_places=2)
    applied_amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance_due = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "credit_memo"
        
