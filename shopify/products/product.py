import json
from ..session.session import Session

class Product:
    def __init__(self, product_data):
        self.__update_data(product_data)

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