import csv, json
from session import Session
from product_list import ProductList

class Importer:
    def import_csv(self, filename: str):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            products_raw_data = []
            for row in csv_reader:
                products_raw_data.append(row)
        data = {
            'products': products_raw_data
        }
        return data

    def import_json(self, filename: str):
        with open(filename, mode='r') as json_file:
            products_raw_data = json.load(json_file)
        return products_raw_data
