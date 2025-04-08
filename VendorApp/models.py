from django.db import models

class VendorApplication(models.Model):
    STATUS_CHOICES = [
         ('PENDING', 'Pending'),
         ('APPROVED', 'Approved'),
         ('REJECTED', 'Rejected'),
    ]

    ORGANIZATION_TYPE_CHOICES = [
        ('Corporation', 'Corporation'),
        ('LLC', 'LLC'),
        ('Sole Proprietorship', 'Sole Proprietorship'),
        ('Partnership', 'Partnership'),
        ('Nonprofit', 'Nonprofit'),
    ]

    application_reference = models.CharField(max_length=50, unique=True, primary_key=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)
    company_name = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=50, blank=True, null=True)  # Fixing field type for consistency
    contact_person = models.CharField(max_length=255)
    title = models.CharField(max_length=100, blank=True, null=True)
    vendor_address = models.TextField()
    phone = models.BigIntegerField()
    fax = models.BigIntegerField(blank=True, null=True)
    vendor_email = models.EmailField()
    tax_exempt = models.BooleanField(default=False)
    vendor_website = models.URLField(blank=True, null=True)
    organization_type = models.CharField(max_length=50, choices=ORGANIZATION_TYPE_CHOICES)  # Use choices
    separate_checks = models.BooleanField(default=False)
    purchasing_card = models.BooleanField(default=False)
    account_no = models.BigIntegerField(blank=True, null=True)
    routing_no = models.IntegerField(blank=True, null=True)
    requestor = models.CharField(max_length=255)
    date_requested = models.DateField()

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'vendor_application'
        managed = True
