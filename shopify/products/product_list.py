import requests
import json
from .product import Product
from ..session.session import Session
from .helpers import extract_url

class ProductList:
    def __init__(self, session: Session, *args, **kwargs):
        self.session = session
        if('imported_data' in kwargs.keys()):
            self.create_from_file(kwargs['imported_data'])

    def __getitem__(self, index: int):
        return self.products[index]

    def get_raw_list(self):
        return [product.get_raw_data() for product in self.products]

    def create_from_file(self, imported_data):
        self.products = [Product(data) for data in imported_data['products']]

    def download_all_products(self):
        response = self.session.get(
            self.session.host + '/admin/api/2020-07/products.json')
        products_all = json.loads(response.text)['products']
        if 'Link' in response.headers.keys():  # if more than 1 page - make requests for the rest
            while 'next' in response.headers['Link']:
                url = extract_url(response.headers['Link'])
                response = self.session.get(url)
                products_from_next_page = json.loads(response.text)['products']
                products_all += products_from_next_page
        self.products = [
            Product(data) for data in products_all
        ]
