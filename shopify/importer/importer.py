import yaml, json
from shopify.session.session import Session
from shopify.products.product_list import ProductList

class Importer:
    def import_yml(self, filename: str):
        with open(filename, mode='r') as yml_file:
            data = yaml.load(yml_file)
        return data

    def import_json(self, filename: str):
        with open(filename, mode='r') as json_file:
            data = json.load(json_file)
        return data
