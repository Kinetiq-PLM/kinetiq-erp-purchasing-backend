import uuid
from django.db import models
from PRF.models import PurchaseRequest  # Import PurchaseRequest model from the PRF app

class RawMaterials(models.Model):
    material_id = models.CharField(max_length=50, primary_key=True)
    material_name = models.CharField(max_length=100)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        db_table = '"admin"."raw_materials"'  # Specify the schema here

    def __str__(self):
        return f"Material {self.material_id}"

class Assets(models.Model):
    asset_id = models.CharField(max_length=50, primary_key=True)
    asset_name = models.CharField(max_length=100)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    class Meta:
        db_table = '"admin"."assets"'  # Specify the schema here

    def __str__(self):
        return f"Asset {self.asset_id}"

class QuotationContent(models.Model):
    quotation_content_id = models.CharField(max_length=255, primary_key=True, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tax_code = models.CharField(max_length=50, null=True, blank=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    # Foreign Keys referencing admin.raw_materials, admin.assets, and purchasing.purchase_requests
    material_id = models.ForeignKey(
        RawMaterials,
        on_delete=models.CASCADE,
        db_column='material_id',
        related_name='quotation_contents',
        null=True,
        blank=True
    )
    asset_id = models.ForeignKey(
        Assets,
        on_delete=models.CASCADE,
        db_column='asset_id',
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

    def calculate_unit_price(self):
        if self.material_id and self.material_id.cost_per_unit:
            return self.purchase_quantity * self.material_id.cost_per_unit
        elif self.asset_id and self.asset_id.purchase_price:
            return self.purchase_quantity * self.asset_id.purchase_price
        return 0  # Default to 0 if no price information is available

    def save(self, *args, **kwargs):
        if not self.quotation_content_id:
            unique_id = uuid.uuid4().hex[:6].upper()
            self.quotation_content_id = f"PURCHASING-QUC-2025-{unique_id}"
        
        self.unit_price = self.calculate_unit_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Quotation Content {self.quotation_content_id}"
    
    class Meta:
        db_table = 'quotation_contents'
        managed = True  # Set to False if you want to manage the table manually
