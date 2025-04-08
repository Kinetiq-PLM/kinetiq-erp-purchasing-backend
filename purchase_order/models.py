from django.db import models
from purchase_quotation.models import PurchaseQuotation  # Assuming the PurchaseQuotation model is in the 'purchasing' app
from datetime import datetime

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    purchase_id = models.CharField(max_length=50, primary_key=True, blank=True)
    quotation_id = models.ForeignKey(PurchaseQuotation, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateField()
    delivery_date = models.DateField()
    document_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        db_table = 'purchase_order'

    def save(self, *args, **kwargs):
        # Auto-generate purchase_id if it doesn't exist
        if not self.purchase_id:
            current_year = datetime.now().year
            last_order = PurchaseOrder.objects.filter(purchase_id__startswith=f"PO-{current_year}").order_by('-purchase_id').first()
            if last_order:
                try:
                    last_number = int(last_order.purchase_id.split('-')[-1])
                except ValueError:
                    last_number = 0
            else:
                last_number = 0

            new_number = last_number + 1
            self.purchase_id = f"PO-{current_year}-{new_number:06d}"

        super().save(*args, **kwargs)

    def __str__(self):
        # Ensure to reference quotation_id's string representation
        quotation_str = str(self.quotation_id) if self.quotation_id else "No Quotation"
        return f"Purchase Order {str(self.purchase_id)}, Quotation {quotation_str}"