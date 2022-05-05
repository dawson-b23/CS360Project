from django import forms 
from django.forms import ModelForm
from .models import Product
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
