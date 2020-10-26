import csv, json
from datetime import datetime
import yaml
from ..session import Session
from ..products.product_list import ProductList
from .helpers import generate_filename, filter_data

class Exporter:
    def __init__(self, products: ProductList):
        self.products = products
        self.variants_headers = ['id', 'sku', 'title', 'price']

    def prepare_data(self):
        filtered_data = filter_data(
            self.products.get_raw_list(), ['id', 'title', 'body_html', 'vendor', 'created_at'], self.variants_headers)
        data = {
            'products': filtered_data
        }
        return data
    
    def export_yml(self):
        filename = generate_filename('.yml')
        with open(filename, mode='w') as products_file:
            data = self.prepare_data()
            yaml.dump(data, products_file)
        return filename

    def export_json(self):
        filename = generate_filename('.json')
        with open(filename, mode='w') as products_file:
            data = self.prepare_data()
            json.dump(data, products_file)
        return filename
