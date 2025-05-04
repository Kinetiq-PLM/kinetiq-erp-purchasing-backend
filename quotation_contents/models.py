import uuid
from datetime import datetime  # Import datetime
from django.db import models
from PRF.models import PurchaseRequest  # Import PurchaseRequest model from the PRF app

class RawMaterials(models.Model):
    item_id = models.CharField(max_length=50, primary_key=True)
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)

    class Meta:
        db_table = '"admin"."item_master_data"'  # Specify the schema here

    def __str__(self):
        return f"Material {self.item_id}"

class QuotationContent(models.Model):
    quotation_content_id = models.CharField(max_length=255, primary_key=True, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tax_code = models.CharField(max_length=50, null=True, blank=True)

    # Foreign Keys referencing admin.raw_materials, admin.assets, and purchasing.purchase_requests
    item_id = models.ForeignKey(
        RawMaterials,
        on_delete=models.CASCADE,
        db_column='item_id',
        related_name='quotation_contents',
        null=True,
        blank=True
    )

    # Foreign Key to PurchaseRequest (from PRF app)
    request_id = models.ForeignKey(
        PurchaseRequest,  # Reference the PurchaseRequest model from the PRF app
        on_delete=models.CASCADE,
        db_column='request_id',
        related_name='quotation_contents',
        default=1
    )

    purchase_quantity = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Add total field

    def save(self, *args, **kwargs):
        # Calculate the total before saving
        if self.unit_price is not None and self.purchase_quantity is not None:
            total = self.unit_price * self.purchase_quantity
            if self.discount:
                total -= total * (self.discount / 100)  # Apply discount if available
            self.total = round(total, 2)  # Save the calculated total

        # Generate a unique quotation_content_id if not already set
        if not self.quotation_content_id:
            unique_id = uuid.uuid4().hex[:6].upper()  # Generate a unique 6-character ID
            self.quotation_content_id = f"PURCHASING-QUC-{datetime.now().year}-{unique_id}"

        super().save(*args, **kwargs)  # Ensure the parent save method is called

    def __str__(self):
        return f"Quotation Content {self.quotation_content_id}"

    class Meta:
        db_table = 'quotation_contents'
        managed = True  # Set to False if you want to manage the table manually