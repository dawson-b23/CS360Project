from django import forms 
from django.forms import ModelForm
from .models import Product, Customer
import random

# create a product form
class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ('PID', 'name', 'brand', 'size', 'price', 'internetAccess', 'shippingCost', 'shippingTime')

		widgets = {
			'PID': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'brand': forms.TextInput(attrs={'class':'form-control'}),
			'size': forms.TextInput(attrs={'class':'form-control'}),
			'price': forms.TextInput(attrs={'class':'form-control'}),
		    'internetAccess': forms.TextInput(attrs={'class':'form-control'}),
		    'shippingCost': forms.TextInput(attrs={'class':'form-control'}),
		    'shippingTime': forms.TextInput(attrs={'class':'form-control'}),
		}


class UserForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('CID', 'firstName', 'lastName', 'email', 'street', 'city', 'state', 'zipCode', 'internetType')

		widgeCts = {
			'CID': forms.TextInput(attrs={'class':'form-control'}),
			'firstName': forms.TextInput(attrs={'class':'form-control'}),
			'lastName': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'})),
			'street': forms.TextInput(attrs={'class':'form-control'}), 
			'city': forms.TextInput(attrs={'class':'form-control'}),
			'state': forms.TextInput(attrs={'class':'form-control'}),
			'zipCode': forms.TextInput(attrs={'class':'form-control'}),
			'internetType': forms.TextInput(attrs={'class':'form-control'}),
		}