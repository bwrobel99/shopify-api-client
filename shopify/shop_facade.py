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
        for (index, product) in enumerate(self.products):
            print(str(index) + product.get_display_info())
        print('\n')

    def edit_product(self):
        product_index = int(input('Enter index of product to edit: '))
        
        try:
            product_chosen = self.products[product_index]
        except IndexError:
            product_index = int(input('Wrong index! Please enter it again: '))
            product_chosen = self.products[product_index]

        print('Product chosen: ' + product_chosen.get_display_info())
        print('What do you want to edit?') 
        attributes = [attr for attr in vars(product_chosen)]
        for (index, attr) in enumerate(attributes):
            print(str(index) + ' ' + attr if attr != "id" else " ")

        attribute_index = int(input('Enter index of product to edit: '))
        attribute_chosen = attributes[attribute_index]
        attribute_new_value = input('Enter new value for attribute: ')
        new_data = {
            'product': {
                'id': product_chosen.id,
            }
        }
        new_data['product'][attribute_chosen] = attribute_new_value
        return product_chosen.edit(self.session, new_data)
        
    def export_csv(self):
        exporter = Exporter(self.products)
        filename = exporter.export_csv()
        return filename

    def export_json(self):
        exporter = Exporter(self.products)
        filename = exporter.export_json()
        return filename

    def import_csv(self, filename):
        importer = Importer()
        imported_data = importer.import_csv(filename)
        self.products = ProductList(self.session, imported_data=imported_data)

    def import_json(self, filename):
        importer = Importer()
        imported_data = importer.import_json(filename)
        self.products = ProductList(self.session, imported_data=imported_data)

    def save_changes_to_server(self):
        for product in self.products:
            product.save_state_to_server(self.session)
