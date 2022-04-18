from django.urls import path

from . import database

urlpatterns = [
	path('', database.home, name="home"),
]