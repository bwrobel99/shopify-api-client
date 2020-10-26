import json
from shopify.exporter.helpers import filter_data

def get_changed_products_ids(product_list, product_list_imported):
    headers = product_list_imported[0].keys()
    variant_headers = product_list_imported[0]['variants'][0].keys()
    product_list_filtered = filter_data(product_list, headers, variant_headers)
    product_ids = [product['id'] for product in product_list_filtered]
    products_changed_ids = []
    for id in product_ids:
        product_present = next(
            (product for product in product_list_filtered if product['id'] == id), None)
        product_present_json = json.dumps(product_present)
        product_imported = next(
            (product for product in product_list_imported if product['id'] == id), None)
        product_imported_json = json.dumps(product_imported)
        if product_present != product_imported:
            products_changed_ids.append(id)
    return products_changed_ids
