class BaseBot:

    def post(self, method, **kwargs):
        raise NotImplementedError

    def get(self, url, data=None, json=None, **kwargs):
        raise NotImplementedError
