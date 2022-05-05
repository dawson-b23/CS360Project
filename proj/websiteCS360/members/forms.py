from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms

class RegisterUserForm(UserCreationForm):
	vendor = False
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	firstName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	lastName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User 
		fields = ('username', 'firstName', 'lastName', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'


class RegisterVendorForm(UserCreationForm):
	vendor = True 
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	firstName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	lastName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User 
		fields = ('username', 'firstName', 'lastName', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
