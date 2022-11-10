import requests
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('../config/config.ini')

# endpoint = config['DEFAULT']['Endpoint']
endpoint = "https://www.cartrawler.com/ctabe/cars.json"

class RequestHandler:
    def __init__(self, url=endpoint):
        self.url = url

    def make_get_request(self):
        return requests.get(self.url).content
