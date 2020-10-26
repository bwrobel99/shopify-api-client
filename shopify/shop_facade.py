from .helpers import get_changed_products_ids
from shopify.session.session import Session
from shopify.products.product_list import ProductList
from shopify.exporter.exporter import Exporter
from shopify.importer.importer import Importer

class ShopFacade:
    def __init__(self, session: Session):
        self.session = session
        self.products = ProductList(self.session)
        self.products.download_all_products()

    def view_all_products(self):
        print('INDEX   ID   TITLE')
        for (index, product) in enumerate(self.products):
            print(str(index) + product.get_display_info())
        print('\n')

    def refresh_product_list(self):
        self.products.download_all_products()

    def edit_product_attributes(self, product_index):
        product_chosen = self.products[product_index]
        new_data = product_chosen.edit_attributes()
        return product_chosen.edit(self.session, new_data)
    
    def clear_product_images(self, product_index):
        product_chosen = self.products[product_index]
        new_data = {
            'product': {
                'id': product_chosen.id,
                'images': []
            }
        }
        return product_chosen.edit(self.session, new_data)
        
    def add_product_image(self, product_index, image_src):
        product_chosen = self.products[product_index]
        new_data = product_chosen.add_image(image_src)
        return product_chosen.edit(self.session, new_data)

    def reorder_product_images(self, product_index):
        product_chosen = self.products[product_index]
        new_data = product_chosen.reorder_images()
        return product_chosen.edit(self.session, new_data)

    def reorder_product_variants(self, product_index):
        product_chosen = self.products[product_index]
        new_data = product_chosen.reorder_variants()
        return product_chosen.edit(self.session, new_data)

    def update_product_and_variant(self, product_index):
        product_chosen = self.products[product_index]
        new_data = product_chosen.update_product_and_variant()
        return product_chosen.edit(self.session, new_data)
        
    def export_yml(self):
        exporter = Exporter(self.products)
        filename = exporter.export_yml()
        return filename

    def export_json(self):
        exporter = Exporter(self.products)
        filename = exporter.export_json()
        return filename

    def import_yml(self, filename):
        importer = Importer()
        imported_data = importer.import_yml(filename)
        self.products_imported = ProductList(self.session, imported_data=imported_data)

    def import_json(self, filename):
        importer = Importer()
        imported_data = importer.import_json(filename)
        self.products_imported = ProductList(
            self.session, imported_data=imported_data)

    def save_imported_changes_to_server(self):
        changed_ids = get_changed_products_ids(self.products.get_raw_list(), self.products_imported.get_raw_list())
        for product in self.products:
            if product.id in changed_ids:
                product.save_state_to_server(self.session)
        return changed_ids