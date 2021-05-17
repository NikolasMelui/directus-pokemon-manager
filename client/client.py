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


application = Application(BASE_URL)
print(str(application))

pokemons = application.get_all()
[print(pokemon) for pokemon in pokemons['data']]
