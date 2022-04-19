from django.shortcuts import render,redirect
from events.models import CustomerDetails

def home(request):
	return render(request, 'events/home.html', {})

def Showcus(request):
	resultsdisplay=CustomerDetails.objects.all()
	return render(request,"tables.html",{'CustomerDetails':resultsdisplay})
