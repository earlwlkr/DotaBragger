import requests


class User(object):
    def __init__(self):
        self.session = requests.session()
    def get(self, url, **kw):
        return self.request('GET', url, **kw)
    def post(self, url, **kw):
        return self.request('POST', url, **kw) 
    def request(self, method, url, **kw):
        assert method in ('GET', 'POST')
        if method == 'GET':
            response = self.session.get(url, **kw)
        elif method == 'POST':
            response = self.session.post(url, **kw)

        assert response.status_code == 200
        return response