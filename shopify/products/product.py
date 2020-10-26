import json
from ..session.session import Session

class Product:
    def __init__(self, product_data):
        self.__update_data(product_data)
        self.updateable_attributes = ['title', 'status', 'vendor', 
                'body_html', 'published_scope', 'tags']
        self.variant_updateable_attributes = ['title', 'price', 'sku']
        
    def __update_data(self, new_data):
        for k, v in new_data.items():
            setattr(self, k, v)

    def edit(self, session: Session, new_data):
        url = session.host + '/admin/api/2020-07/products/' + str(self.id) + '.json'
        response = session.put(url, data=json.dumps(new_data))
        updated_data = json.loads(response.text)
        self.__update_data(updated_data['product'])
        return response.status_code

    def save_state_to_server(self, session: Session):
        url = session.host + '/admin/api/2020-07/products/' + \
            str(self.id) + '.json'
        data = {
            'product': self.get_raw_data()
        }
        response = session.put(url, data=json.dumps(data))
        return response.status_code

    def get_raw_data(self):
        return self.__dict__

    def get_display_info(self):
        return ' ' + str(self.id) + ' ' + self.title

    def edit_attributes(self):
        attributes = [attr for attr in self.updateable_attributes]
        for (index, attr) in enumerate(attributes):
            if attr != "id":
                print(str(index) + ' ' + attr)

        attribute_index = int(input('Enter index of attribute to edit: '))
        attribute_chosen = attributes[attribute_index]
        attribute_new_value = input('Enter new value for attribute: ')
        new_data = {
            'product': {
                'id': self.id,
            }
        }
        new_data['product'][attribute_chosen] = attribute_new_value
        return new_data

    def update_product_and_variant(self):
        new_data = self.edit_attributes()
        variants = [{"id": variant['id']}
                    for variant in self.get_raw_data()['variants']]
        print('Product variants:')
        print(*variants)
        variant_index = int(
            input('Choose variant to edit: '))
        print(self.variant_updateable_attributes)
        attribute_index = int(
            input('Choose attribute to edit: '))
        attribute_chosen = self.variant_updateable_attributes[attribute_index]
        variants[variant_index][attribute_chosen] = input(
            'Enter new value for attribute: ')
        new_data["variants"] = variants
        return new_data

    def reorder_variants(self):
        product_variants = self.get_raw_data()['variants']
        print('Current order:')
        order = [(index, variant['id']) for (index, variant) in enumerate(product_variants)]
        print(*order)
        new_order = []
        for variant in product_variants:
            new_position = int(
                input('Input new index for ' + str(variant['id']) + ': '))
            new_order.append(new_position)
        product_variants_ordered = [product_variants[i] for i in new_order]
        new_data = {
            'product': {
                'id': self.id,
                'variants': product_variants_ordered
            }
        }
        return self.edit(self.session, new_data)

    def reorder_images(self):
        product_images = self.get_raw_data()['images']
        print('Current order:')
        order = [{'id': image['id'], 'position': image['position']} for image in product_images]
        print(*order)
        for image in order:
            new_position = int(input('Input new index for ' + str(image['id']) + ': '))
            image['position'] = new_position
        new_data = {
            'product': {
                'id': self.id,
                'images': order
            }
        }
        return self.edit(self.session, new_data)

    def add_image(self, image_src):
        product_images = self.get_raw_data()['images']
        product_images.append({
            'src': image_src
        })
        new_data = {
            'product': {
                'id': self.id,
                'images': product_images
            }
        }
        return self.edit(self.session, new_data)
