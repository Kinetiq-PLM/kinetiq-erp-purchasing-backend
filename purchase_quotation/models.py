from django.db import models


class Vendor(models.Model):
    vendor_code = models.CharField(max_length=50, primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[("Approved", "Approved"), ("Under Review", "Under Review"), ("Rejected", "Rejected")],
        default="Approved",
    )

    class Meta:
        db_table = '"purchasing"."vendors"'

    def __str__(self):
        return self.vendor_code

class PurchaseQuotation(models.Model):
    quotation_id = models.CharField(max_length=50, primary_key=True)
    vendor_code = models.ForeignKey(
        Vendor,  # ForeignKey to Vendor
        on_delete=models.CASCADE,
        db_column='vendor_code'
    )
    status = models.CharField(
        max_length=50,
        choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected"), ("Completed", "Completed")],
        default="Pending",
    )
    downpayment_request = models.IntegerField(default=0, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    delivery_loc = models.CharField(max_length=255, blank=True, null=True)
    document_no = models.IntegerField( blank=True, null=True)  # Document number
    valid_date = models.DateField()
    document_date = models.DateField()
    required_date = models.DateField()
    total_before_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    freight = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    request_id = models.ForeignKey(
        'PRF.PurchaseRequest',  # Use a string reference to avoid circular imports
        on_delete=models.CASCADE,
        db_column='request_id',
        related_name='purchase_quotations',
        default=None,
    )

    def save(self, *args, **kwargs):
        # Recalculate total_payment
        self.total_payment = (
            self.total_before_discount - (self.total_before_discount * (self.discount_percent / 100))
            + self.freight + self.tax
        )

        # Auto-generate document_no if it doesn't exist
        if not self.document_no:
            last_quotation = PurchaseQuotation.objects.order_by('-document_no').first()  # Get the last document_no
            if last_quotation and last_quotation.document_no:
                self.document_no = last_quotation.document_no + 1
            else:
                self.document_no = 1  # Start from 1 if no document_no exists

        # Generate quotation_id if it doesn't exist
        if not self.quotation_id:
            last_quotation = PurchaseQuotation.objects.filter(
                quotation_id__startswith="PURCHASING-PUQ-2025"
            ).order_by('-quotation_id').first()  # Use descending order
            if last_quotation:
                try:
                    last_number = int(last_quotation.quotation_id.split('-')[-1])
                except ValueError:
                    last_number = 0
            else:
                last_number = 0  # If no existing quotations

            new_number = last_number + 1
            self.quotation_id = f"PURCHASING-PUQ-2025-{new_number:06d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Quotation {self.quotation_id}"

    class Meta:
        db_table = '"purchasing"."purchase_quotation"'