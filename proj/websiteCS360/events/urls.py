from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #path('',views.Showcus),
    path('contactUs', views.contactUs, name="contactUs"),
    path('gitAccess', views.gitAccess, name="gitAccess"),
    path('aboutUS', views.aboutUs, name='aboutUs'),
    path('ERDiagram', views.ERDiagram, name='ERDiagram'),
    path('ProductList', views.ProductList, name='ProductList'),
]
