from django.db import connections
from django.db import models

##
##  These are for the products and services (interaction with customer)
##

class Product(models.Model):
    PID = models.IntegerField(primary_key=True) # PK
    name = models.TextField(max_length=120)
    size = models.TextField(max_length=60)
    brand = models.TextField(max_length=120)
    price = models.TextField(max_length=1000)
    internetAccess = models.TextField(max_length=100)
    shippingCost = models.TextField(max_length=100)
    shippingTime = models.TextField(max_length=100)


    def __str__(self):
        return self.name

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
    CID = models.IntegerField(primary_key=True)
    firstName = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    street = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    state = models.TextField(max_length=100)
    zipCode = models.TextField(max_length=100)
    internetType = models.TextField(max_length=100)


    def __int__(self):
        return self.firstName + '' + self.lastName


class Vendor(models.Model):
    VID = models.IntegerField(primary_key=True)
    companyName = models.TextField(max_length=100)
    CID = models.IntegerField()
    PID = models.IntegerField()
    #CID = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    #PID = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True)


    def __str__(self):
        return self.companyName


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
    #delivery = FK?
    CID = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)


    def __str__(self):
        return self.RID
'''
'''
class Delivery(models.Model):
    DID = models.IntegerField(primary_key=True)
    shippingCost = models.TextField(max_length=100)
    shippingTime = models.TextField(max_length=100)


    def __int__(self):
        return self.DID
'''

