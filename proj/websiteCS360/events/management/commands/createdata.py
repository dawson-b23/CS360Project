
'''
import random

from faker.providers import BaseProvider
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()
#from events import settings
#from events.models import Product, Customer, Vendor, Delivery





PRODUCTS = [
    "Camera",
    "Smart Phone",
    "Laptop",
    "PC",
    "Flat Screen TV",
    "Smart TV",
    "VCR",
    "Record Player",
    "DVR",
    "Tablet",
    "Telescope",
    "Printer",
    "Oven",
    "Stove",
    "Refrigerator",
    "Microwave",
    "Headphones",
    "Bluetooth Earphones",
    "Watch",
    "SmartWatch",
    "Drone",
    "Head-Set",
    "Robot Cleaner",
    "Home Security System",
    "Video Doorbell",
    "Blender",
    "Air Fryer",
    "Bread Maker",
    "Cast Iron Skillet",
    "Cast Iron Pot",
    "Toaster",
    "Coffee Maker",
]


BRANDS = [
    "Apple",
    "Microsoft",
    "Samsung",
    "Intel",
    "Sony",
    "Amazon",
    "Bose",
    "Canon",
    "Dynex",
    "Dyson",
    "Epson",
    "GoPro",
    "HP",
    "Insignia",
    "iRobot",
    "Keurig",
    "Lenovo",
    "LG",
    "Nikon",
    "Nintendo",
    "RocketFish",
    "Sharp",
    "Sonos",
    "Vizio",
    "Whirlpool",
]


SIZE = [
    "1920x1080",
    "1366x768",
    "1440x900",
    "1536x864",
    "1024x768",
    "5 in.",
    "10 in.",
    "15 in.",
    "20 in.",
    "25 in.",
    "30 in.",
    "35 in.",
    "40 in.",
    "45 in.",
    "50 in.",
    "55 in.",
    "60 in.",
    "65 in.",
    "70 in.",
    "75 in.",
    "80 in.",
    "85 in.",
    "90 in.",
    "95 in.",
    "100 in.",  
]


SHIPPINGTIME = [
    "1-2 days",
    "3-5 days",
    "1 week",
    "1-2 weeks",
    "3 weeks",
    "4 weeks",
    "3-4 weeks",
    "5 weeks",
    "6 weeks",
    "5-6 weeks",
]

INTERNETACCESS = [
    "Yes",
    "No",
]

INTERNETYPE = [
    "Cable",
    "Dial-up",
    "DSl",
    "Fiber-optics",
    "Fixed wireless",
    "Satellite",
]

INTERNETCOST = [
    "$10/month"
    "$20/month",
    "$30/month",
    "$40/month",
    "$50/month",
    "$60/month",
    "$70/month",
    "$80/month",
    "$90/month",
    "$100/month",
    "$110/month",
    "$120/month",
    "$130/month",
    "$120/month",
    "$130/month",
    "$140/month",
    "$150/month",
    "$160/month",
    "$170/month",
    "$180/month",
    "$190/month",
    "$200/month",
]



class MyProvider(faker.providers.BaseProvider):
    def store_products(self):
        return self.random_element(PRODUCTS)

    def store_brands(self):
        return self.random_element(BRANDS)

    





class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        
        #fake = Faker(["nl_NL"])
        fake.add_provider(MyProvider)
        print(fake.store_products())
   '''