import os
import random
import sys
import django 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from csv_parser import csv_parser
from website.models import Product, Category

# import csv_parser from './csv_parser.py'
def create_products():
    print("⚡ Creating products...")

    products = csv_parser('products.csv')

    for product in products:
        entry = Product()

        entry.name = product['name']
        entry.price = float(product['price'].replace(",","") or 0)
        entry.stock = random.randrange(1, 99)
        entry.image_url = product['img_source']

        entry.save()

        # create multiple categories
        categories = list()
        for category in product['breadcrumbs'].strip().split(' | '):
            if category:
                newCategory, created = Category.objects.get_or_create(name=category)
                categories.append(newCategory)

        entry.categories.set(categories)

    print("✅ Products created!")

create_products()
