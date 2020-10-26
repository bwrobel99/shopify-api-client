import json
from shopify.exporter.helpers import filter_data

def get_changed_products_ids(product_list, product_list_imported):
    headers = product_list_imported[0].keys()
    variant_headers = product_list_imported[0]['variants'][0].keys()
    product_list_filtered = filter_data(product_list, headers, variant_headers)
    differences = []
    for i in range(len(product_list_imported)):
        diffkeys = {
            product_list_filtered[i]['id']: k for k in product_list_filtered[i] if product_list_filtered[i][k] != product_list_imported[i][k]}
        differences += diffkeys
    return differences
