import requests
import sys
from shopify.session.helpers import validate_host

class Session(requests.Session):
    def __init__(self, host: str, access_token: str, *args, **kwargs):
        super(Session, self).__init__(*args, **kwargs)
        self.host = host
        self.access_token = access_token
        self.headers.update({
            'X-Shopify-Access-Token': self.access_token,
            'content-type': 'application/json'
        })

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if not validate_host(value):
            value = 'https://' + value
        self._host = value
