import uuid
from django.db import models
from purchase_order.models import PurchaseOrder  # adjust import if needed
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Shipment(models.Model):
    def generate_shipment_id():
        # Generate a shipment ID with format: PURCHASING-RES-<YEAR>-<increment>
        year = timezone.now().year
        last_shipment = Shipment.objects.filter(shipment_id__startswith=f"PURCHASING-RES-{year}").last()
        increment = 1
        if last_shipment:
            try:
                increment = int(last_shipment.shipment_id.split('-')[-1]) + 1
            except (ValueError, IndexError):
                increment = 1
        return f"PURCHASING-RES-{year}-{str(increment).zfill(3)}"

    shipment_id = models.CharField(primary_key=True, max_length=100, default=generate_shipment_id)
    delivery_date = models.DateField()
    purchase_id = models.ForeignKey(
        PurchaseOrder, 
        on_delete=models.CASCADE,
        db_column='purchase_id'
    )

    def __str__(self):
        return self.shipment_id

    class Meta:
        db_table = 'received_shipments'
       

@receiver(pre_save, sender=Shipment)
def set_shipment_id(sender, instance, **kwargs):
    if not instance.shipment_id:
        instance.shipment_id = Shipment.generate_shipment_id()
