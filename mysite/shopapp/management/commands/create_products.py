from typing import Any
from django.core.management import BaseCommand

from shopapp.models import Product

class Command(BaseCommand):
    """
    Creates products
    """
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Create products")

        products_names = [
            "Laptop",
            "Desktop",
            "Smartphone"
        ]
        for products_name in products_names:
            product, created = Product.objects.get_or_create(name=products_name)
            self.stdout.write(f"Creted product {product.name}")
        
        self.stdout.write(self.style.SUCCESS("Product created"))
