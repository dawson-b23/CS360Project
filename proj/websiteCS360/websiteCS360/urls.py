from django.contrib import admin
from django.urls import path, include
#from django.urls import path
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
