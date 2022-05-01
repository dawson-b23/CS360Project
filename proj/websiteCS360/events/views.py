from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseRedirect
#from events.models import CustomerDetails

def home(request):
	return render(request, 'events/home.html', {})


def contactUs(request):
	return render(request, 'events/contactUs.html', {})


def gitAccess(request):
	return render(request, 'events/gitAccess.html', {})


def aboutUs(request):
	return render(request, 'events/aboutUs.html', {})


def ERDiagram(request):
	return render(request, 'events/ERDiagram.html', {})

	
def ProductList(request):
	productList = Product.objects.all()
	return render(request, 'events/ProductList.html', 
		{'productList': productList})


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
