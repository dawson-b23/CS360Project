from django.db import connections
from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    CustomerID=models.CharField(max_length=100)
    CustomerName=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Budget=models.CharField(max_length=100)
    class Meta:
        db_table="customer"
