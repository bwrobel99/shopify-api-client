import requests
import json
from session import Session
from product import Product

class ProductList:
    def __init__(self, session: Session, *args, **kwargs):
        self.session = session
        if('imported_data' in kwargs.keys()):
            self.create_from_file(kwargs['imported_data'])

    def __getitem__(self, index: int):
        return self.products[index]

    def get_raw_list(self):
        return [product.get_daw_data() for product in self.products]

    def create_from_file(self, imported_data):
        self.products = [Product(data) for data in imported_data['products']]

    def download_all_products(self):
        response = self.session.get(
            self.session.host + '/admin/api/2020-07/products.json')
        products = json.loads(response.text)
        self.products = [Product(data) for data in products['products']]
