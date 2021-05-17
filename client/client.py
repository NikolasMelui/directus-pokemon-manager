import os
import requests

from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.environ.get('BASE_URL')


class Application:
    def __init__(self, url):
        self.url = url

    def get_all(self):
        r = requests.get(f'{self.url}/items/pokemons')
        return r.json()

    def get_by_id(self, id):
        r = requests.get(f'{self.url}/items/pokemons/{id}')
        return r.json()

    def know_more(self, name):
        r = requests.get(f'{self.url}/custom/know-more/{name}')
        return r.json()


application = Application(BASE_URL)

pokemons = application.get_all()
[print(pokemon) for pokemon in pokemons['data']]

# info = application.get_by_id(1)
# print(info)

# info = application.know_more('magmar')
# print(info)
