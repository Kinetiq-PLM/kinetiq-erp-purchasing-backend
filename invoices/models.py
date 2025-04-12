from django.db import models
import datetime  

class DocumentItems(models.Model):
    content_id = models.CharField(max_length=30, primary_key=True)

    class Meta:
        db_table = 'document_items'
        managed = False 

class APInvoice(models.Model):
    invoice_id = models.CharField(max_length=30, primary_key=True)  



    status = models.CharField(
        max_length=20,
        choices=[("Open", "Open"), ("Closed", "Closed"), ("Cancelled", "Cancelled"), ("Draft", "Draft")],
        default="Draft",
    )
    content_id = models.ForeignKey(
        DocumentItems,
        to_field='content_id',
        db_column='content_id',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    document_no = models.IntegerField(default=0)
    document_date = models.DateField(default=datetime.date.today)
    due_date = models.DateField(default=datetime.date.today)
    total_credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    credit_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    dpm_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    dpm_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    applied_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    balance_due = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.invoice_id

    
    class Meta:
        db_table = 'purchase_invoice'  # This is the name of the table in PostgreSQL

        managed = True # Ensure Django manages the table if needed
