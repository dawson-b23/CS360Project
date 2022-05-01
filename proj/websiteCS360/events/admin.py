from django.contrib import admin
from .models import Customer
from .models import Vendor
#from .models import Wishlist
from .models import Requirement
from .models import Product
#from .models import Service
from .models import Delivery

admin.site.register(Customer)
admin.site.register(Vendor)
#admin.site.register(Wishlist)
admin.site.register(Requirement)
admin.site.register(Product)
#admin.site.register(Service)
admin.site.register(Delivery)
