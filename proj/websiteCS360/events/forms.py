from django import forms 
from django.forms import ModelForm
from .models import Product

# create a product form
class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ('PID', 'name', 'brand', 'size', 'price')

		widgets = {
			'PID': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'brand': forms.TextInput(attrs={'class':'form-control'}),
			'size': forms.TextInput(attrs={'class':'form-control'}),
			'price': forms.TextInput(attrs={'class':'form-control'})
		}
