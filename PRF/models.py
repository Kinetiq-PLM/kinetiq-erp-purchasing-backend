from django.db import models
from datetime import date
# Employee model
class Employee(models.Model):
    employee_id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    dept_id = models.CharField(max_length=255, blank=True, null=True)  # Assuming this is a string field
    employment_type = models.CharField(max_length=50, blank=True, null=True)  # Assuming this is a string field
    status = models.CharField(max_length=50, blank=True, null=True)  # Assuming this is a string field

    class Meta:
        db_table = '"human_resources"."employees"'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"


class PurchaseRequest(models.Model):
     # Status choices
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Acknowledged", "Acknowledged"),
        ("Approved", "Approved"),
        ("Finished", "Finished"),
        ("Cancelled", "Cancelled"),
        ("Rejected", "Rejected"),
        ("Returned", "Returned"),
        ("Expired", "Expired"),
    ]

    request_id = models.CharField(max_length=50, primary_key=True, blank=True)
    employee_id = models.CharField(max_length=50, blank=True, null=True)  # Changed to character varying
    valid_date = models.DateField()
    document_date = models.DateField()
    required_date = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Pending",  # Default status
    )

    def save(self, *args, **kwargs):
        # Automatically update status to "Expired" if valid_date has passed
        if self.valid_date and self.valid_date < date.today() and self.status != "Expired":
            self.status = "Expired"
            print(f"Status automatically updated to 'Expired' for Request ID: {self.request_id}")

        if not self.request_id:
            last_request = PurchaseRequest.objects.filter(request_id__startswith="PURCHASING-PUR-").order_by('-request_id').first()
            if last_request:
                try:
                    last_number = int(last_request.request_id.split('-')[-1])
                except ValueError:
                    last_number = 0
            else:
                last_number = 0

            new_number = last_number + 1
            self.request_id = f"PURCHASING-PUR-{new_number:06d}"
        else:
            print(f"Using manually provided Request ID: {self.request_id}")

        print(f"Saving Request ID: {self.request_id}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Request {self.request_id}"

    class Meta:
        db_table = '"purchasing"."purchase_requests"'
