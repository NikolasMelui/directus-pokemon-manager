import os
import json
import requests

from dotenv import load_dotenv
load_dotenv()

POKEAPI_URL = os.environ.get('POKEAPI_URL')
DIRECTUS_URL = os.environ.get('DIRECTUS_URL')
SECRET_TOKEN = os.environ.get('SECRET_TOKEN')

LIMIT = 10


def get_pokemons():
    r = requests.get(f'{POKEAPI_URL}/pokemon?limit={LIMIT}')
    return r.json()


def load_pockemon(pokemon):
    r = requests.post(f'{DIRECTUS_URL}/items/pokemons', data=json.dumps({
        'name': pokemon['name'],
        'url': pokemon['url']
    }), headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SECRET_TOKEN}'
    })
    print(r.text)


pokemons = get_pokemons()
[load_pockemon(pokemon) for pokemon in pokemons['results']]
