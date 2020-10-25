from datetime import datetime

def generate_filename(extension: str):
    now = datetime.now()  # filename will include a timestamp, to avoid overwriting
    timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")
    return 'products_' + timestamp + extension

def filter_data(raw_product_list, headers, variant_headers):
    filtered_product_list = []
    for product in raw_product_list:
        product_filtered_data = {
            header: product[header] for header in headers
        }
        product_filtered_variants = []
        for variant in product['variants']:
            filtered_variants = {
                variant_header: variant[variant_header] for variant_header in variant_headers
            }
            product_filtered_variants.append(filtered_variants)
        product_filtered_data['variants'] = product_filtered_variants
        filtered_product_list.append(product_filtered_data)
    return filtered_product_list
