from django.shortcuts import render
import calendar

from calendar import HTMLCalendar
from datetime import datetime 

from django.http import HttpResponse

def home(request, year, month):
	name = "john"
	month = month.capitalize()

	month_number = list(calender.month_name)
	month_number = int(month_num)

	cal = HTMLCalender().formatmonth(
		year,
		month_number)

	now = datetime.now()
	current_year = now.year

	time = now.strftime('%I:%M:%S %p')
	return render(request,
		'home.html', {
		"name": name,
		"year": year,
		"month": month,
		"month_number": month_number,
		"cal": cal,
		"current_year": current_year,
		"time": time,
		})




