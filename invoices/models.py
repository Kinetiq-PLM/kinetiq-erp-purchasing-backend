from django.db import models
import datetime


class DocumentHeader(models.Model):
    document_id = models.CharField(max_length=30, primary_key=True)
    purchase_id = models.CharField(max_length=30, blank=True, null=True)  # character varying

    class Meta:
        db_table = 'operations"."document_header'
        managed = False  # Django will not manage this table
        


class APInvoice(models.Model):
    invoice_id = models.CharField(max_length=30, primary_key=True)  # character varying
    document_no = models.IntegerField(default=0)  # integer
    document_date = models.DateField(default=datetime.date.today)  # date
    due_date = models.DateField(default=datetime.date.today)  # date
    total_credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # numeric
    credit_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # numeric
    dpm_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # numeric
    dpm_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # numeric
    applied_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # numeric
    balance_due = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # numeric
    status = models.CharField(
        max_length=20,
        choices=[
            ("Open", "Open"),
            ("Closed", "Closed"),
            ("Cancelled", "Cancelled"),
            ("Draft", "Draft"),
        ],
        default="Draft",
    )  # purchase_invoice_status
    document_id = models.ForeignKey(
        DocumentHeader,  # FK to operations.document_header
        to_field='document_id',  # Use document_id as the FK field
        db_column='document_id',  # Map to document_id column in the database
        on_delete=models.SET_NULL,  # Set to NULL if the related document is deleted
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.invoice_id

    class Meta:
        db_table = 'purchase_invoice'  # This is the name of the table in PostgreSQL
        managed = True  # Ensure Django manages the table if needed