import requests

from .BotInterface import BaseBot


class VkBot(BaseBot):
    def __init__(self, access_token='',
                 version_api='5.131'):
        self.access_token = access_token
        self.version_api = version_api
        self.url = 'https://api.vk.com/method/'

    def get(self, method, **kwargs):
        params = {
            'v': self.version_api,
            'access_token': self.access_token,
        }

        params.update(kwargs)

        response = requests.get(
            url=self.url + method,
            params=params,
        )
        return response

    def post(self, url, data=None, json=None, **kwargs):
        response = requests.post(
            url,
            data,
            json,
        )
        return response
