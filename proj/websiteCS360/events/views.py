from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Product, Customer
from .forms import ProductForm, UserForm
from django.http import HttpResponseRedirect
from .filters import OrderFilter
#from events.models import CustomerDetails

def home(request):
	return render(request, 'events/home.html', {})


def contactUs(request):
	return render(request, 'events/contactUs.html', {})


def gitAccess(request):
	return redirect('https://github.com/dawson-b23/CS360Project')


def aboutUs(request):
	return render(request, 'events/aboutUs.html', {})


def ERDiagram(request):
	return redirect('https://lucid.app/lucidchart/9e2c44d2-277b-4d03-a168-4751f80192dc/edit?docId=9e2c44d2-277b-4d03-a168-4751f80192dc&shared=true&invitationId=inv_2a884bc1-cffb-43a0-9be2-78b589fed611&page=0_0#')

	
def ProductList(request):
	productList = Product.objects.all()

	myFilter = OrderFilter(request.GET, queryset=productList)
	productList = myFilter.qs

	return render(request, 'events/ProductList.html', {'productList': productList, 'myFilter': myFilter})


def addProduct(request):
	submitted = False
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/addProduct?submitted=True')
	else:
		form = ProductForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'events/addProduct.html', {'form':form, 'submitted':submitted})


def addUserToDatabase(request):
	submitted = False 
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/addUserToDatabase?submitted=True')
	else:
		form = UserForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'events/addUserToDatabase.html', {'form':form, 'submitted':submitted})


def addVendorToDatabase(request):
	submitted = False 
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/addVendorToDatabase?submitted=True')
	else:
		form = UserForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'events/addVendorToDatabase.html', {'form':form, 'submitted':submitted})