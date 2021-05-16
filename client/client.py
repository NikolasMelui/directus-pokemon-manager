import requests

BASE_URL = "http://localhost:3000/"

def get_pokemons():
  r = requests.get(f'{BASE_URL}items/pokemons')
  return r.json()


pokemons = get_pokemons()
[print(pokemon) for pokemon in pokemons['data']]

