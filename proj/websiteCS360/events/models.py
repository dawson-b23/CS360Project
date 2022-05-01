from django.db import connections
from django.db import models

'''
# Create your models here.
class CustomerDetails(models.Model):
    CustomerID=models.CharField(max_length=100)
    CustomerName=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Budget=models.CharField(max_length=100)
    class Meta:
        db_table="customer"
'''

##
##  These are for the products and services (interaction with customer)
##

class Product(models.Model):
    PID = models.CharField('Product ID', max_length=20) # PK
    name = models.CharField('Product Name', max_length=120)
    #size = 
    brand = models.CharField('Brand', max_length=120)
    price = models.CharField('Price', max_length=12)
    #electronicType = #reliant on options 
    #display = 


    def __str__(self):
        return self.PID

'''
class Service(models.Model):
    SID = models.CharField('Product Name', max_length=120)
    speed = 
    packages = reliant on options?
    contract = 
    cost = 
    internetAccess = 
'''


##
##  These are for the 'backened' of the website (needed for website/best buy)
##

class Customer(models.Model):
    CID = models.CharField('CID', max_length=30)
    firstName = models.CharField('First Name', max_length=120)
    lastName = models.CharField('Last Name', max_length=120)
    email = models.EmailField('Email Address')
    street = models.CharField('Street', max_length=300)
    city = models.CharField('City', max_length=30)
    state = models.CharField('State', max_length=15)
    zipCode = models.CharField('Zip Code', max_length=10)


    def __str__(self):
        return self.CID


class Vendor(models.Model):
    VID = models.CharField('VID', max_length=30)
    companyName = models.CharField('Company Name', max_length=120)
    CID = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    PID = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True)


    def __str__(self):
        return self.VID


'''
class wishList(models.Model):
    WID = # PK
    priority1 = 
    priority2 =
    priority3 = all FK's
    priority4 =
    priority5 =
    CID = models.ForeignKey(Customer, blank=True, null=True)
'''
'''
class Requirement(models.Model):
    RID = models.CharField('Requirement ID', max_length=120)
    size = models.CharField('Requirement Size', max_length=120)
    brand = models.CharField('Requirement Brand', max_length=120)
    price = models.CharField('Requirement Price', max_length=120)
    #electronicType = other options
    #display = 
    #delivery = FK?
    CID = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)


    def __str__(self):
        return self.RID
'''

class Delivery(models.Model):
    DID = models.CharField('Delivery ID', max_length=30)
    shippingCost = models.CharField('Shipping Cost', max_length=30)
    shippingTime = models.CharField('Shipping Time', max_length=30)


    def __str__(self):
        return self.DID


