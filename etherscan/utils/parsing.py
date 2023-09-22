import requests


class ResponseParser:
    @staticmethod
    def parse(response: requests.Response):
        content = response.json()
        return content
