# Import Django's built-in models module to define database models
from django.db import models  
from django.core.exceptions import ValidationError


# Define the `Item` model, representing a database table for storing item details
class Item(models.Model):  
    name = models.CharField(max_length=100)                     # `name` - A character field with a max length of 100 (cannot be null)

    description = models.TextField(blank=True, null=True)       # `description` - A text field (can be left blank or null)

    quantity = models.PositiveIntegerField(default=0)      # `quantity` - A positive integer field with a default value of 0

    price = models.DecimalField(max_digits=10, decimal_places=2)  # `price` - A decimal field with up to 10 digits, 2 of which are after the decimal point

    min_stock_threshold = models.PositiveIntegerField(default=5)  # Business Rule: Low stock warning

    added_on = models.DateTimeField(auto_now_add=True)  # `added_on` - A timestamp that is automatically set when a new record is created

    def __str__(self):  # Define the string representation of an item (for Django admin & shell readability)
        return self.name  
    
    def check_stock(self, order_qty):
        """Business logic: Check if stock is sufficient for an order"""
        if order_qty > self.quantity:
            raise ValidationError(f"Not enough stock for {self.name}. Only {self.quantity} left.")

    def reduce_stock(self, order_qty):
        """Reduce stock when an item is purchased"""
        self.check_stock(order_qty)  # Ensure we have enough
        self.quantity -= order_qty
        self.save()

    def is_low_stock(self):
        """Check if stock is below the minimum threshold"""
        return self.quantity <= self.min_stock_threshold
