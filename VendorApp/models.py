from django.db import models
import uuid
from datetime import datetime

class VendorApplication(models.Model):
    STATUS_CHOICES = [
        ('Under Review','UNDER REVIEW'),
        ('Approved','APPROVED'),
        ('Rejected', 'REJECTED'),
    ]

    vendor_code = models.CharField(max_length=50, primary_key=True, unique=True, blank=True, null=False)  # Primary key
    company_name = models.CharField(max_length=255)  # character varying
    tax_number = models.CharField(max_length=50, blank=True, null=True)  # character varying
    contact_person = models.CharField(max_length=255)  # character varying
    vendor_address = models.CharField(max_length=255)  # character varying
    phone = models.CharField(max_length=50)  # character varying
    vendor_email = models.EmailField()  # character varying
    tax_exempt = models.BooleanField(default=False)  # boolean
    purchasing_card = models.CharField(max_length=50, blank=True, null=True)  # character varying
    account_no = models.CharField(max_length=50, blank=True, null=True)  # character varying
    routing_no = models.CharField(max_length=50, blank=True, null=True)  # character varying
    requestor = models.CharField(max_length=255)  # character varying
    date_requested = models.DateField()  # date
    payment_terms = models.IntegerField(blank=True, null=True)  # integer
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)  # vendor_application_st

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            # Generate a unique vendor code in the format: PURCHASING-VEP-YYYY-<unique_id>
            current_year = datetime.now().year
            unique_id = uuid.uuid4().hex[:6]  # Generate a unique 6-character ID
            self.vendor_code = f"PURCHASING-VEP-{current_year}-{unique_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'vendors'
        managed = True