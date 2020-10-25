import csv, json
from datetime import datetime
from session import Session
from product_list import ProductList
from ehelpers import generate_filename, filter_data

class Exporter:
    def __init__(self, products: ProductList):
        self.products = products
        self.variants_headers = ['id', 'sku', 'title', 'price']

    def export_csv(self):
        filename = generate_filename('.csv')
        with open(filename, mode='w') as products_file:
            products_writer = csv.writer(products_file)
            products_writer.writerow(
                ['id', 'title', 'body_html', 'vendor', 'created_at', 'variants'])
            for product in self.products:
                variants_data = []
                for variant in product.variants:
                    variants_data.append({var_hdr: variant.get(var_hdr) for var_hdr in self.variants_headers})
                products_writer.writerow(
                    [product.id, product.title, product.body_html, product.vendor, product.created_at, variants_data])
        return filename

    def export_json(self):
        filename = generate_filename('.json')
        filtered_data = filter_data(
            self.products.get_raw_list(), ['id', 'title', 'body_html', 'vendor', 'created_at'], self.variants_headers)
        data = {
            'products' : filtered_data
        }
        with open(filename, mode='w') as products_file:
            json.dump(data, products_file)
        return filename
