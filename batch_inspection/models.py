import uuid
from django.db import models
from django.utils import timezone
from received_shipments.models import Shipment
from PRF.models import Employee  # Adjust the import path if needed

class Inspection(models.Model):
    def generate_inspection_id():
        # Generate an inspection ID with format: INSPECTION-<YEAR>-<increment>
        year = timezone.now().year
        # Get the latest inspection (if any) and calculate the next increment
        last_inspection = Inspection.objects.filter(inspection_id__startswith=f"INSPECTION-{year}").last()
        increment = 1
        if last_inspection:
            # Extract the increment number from the last inspection's ID and increase it by 1
            increment = int(last_inspection.inspection_id.split('-')[-1]) + 1
        # Format the new inspection ID
        return f"INSPECTION-{year}-{str(increment).zfill(3)}"

    inspection_id = models.CharField(primary_key=True, max_length=100, default=generate_inspection_id)
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE, db_column='shipment_id', related_name='inspections_id')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='employee_id', related_name='inspections_id')
    inspection_date = models.DateField()
    inspection_result = models.CharField(max_length=100)
    remarks = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.inspection_id

    class Meta:
        db_table = 'batch_inspection'  # Ensure this table name is unique
