from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Product
#from events.models import CustomerDetails

def home(request):
	return render(request, 'events/home.html', {})

'''
def Showcus(request):
	resultsdisplay=CustomerDetails.objects.all()
	return render(request,"tables.html",{'CustomerDetails':resultsdisplay})
'''

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
