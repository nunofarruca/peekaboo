import json
import logging
import requests
from bs4 import BeautifulSoup

CONFIG_PATH = "./stores/config/ikea_config.json"


class Ikea:
    items = {}

    def __init__(self):
        with open(CONFIG_PATH) as json_file:
            try:
                self.items = json.load(json_file)
            except Exception as e:
                logging.error(f"{e} is missing")
                exit(0)

    def peek(self):
        logging.info("Ikea peek running.")
        for key, url in self.items.items():
            # print(key + ' > ' + url)
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')
            div = soup.find('div', class_='js-available-for-delivery')

            # print(div.prettify())

            if 'unavailable' in div.text:
                print(key + ' > ' + 'ohhhh')
            elif 'Available' in div.text:
                print(key + ' > ' + 'buy buy buy')
            else:
                print(key + ' > ' + 'crash and burn')
