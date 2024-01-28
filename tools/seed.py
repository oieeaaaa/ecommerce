import os
import random
import sys
import django 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from csv_parser import csv_parser
from website.models import Product

# import csv_parser from './csv_parser.py'

def create_product():
    products = csv_parser('product_playground.csv')

    for product in products:
        Product.objects.create(
                name=product['name'], 
                price=float(product['price'].replace(",","") or 0), 
                stock=random.randrange(1, 99), 
                image_url=product['img_source']
        )

print("nope.")
# create_product()
