import requests

BASE_URL = "http://localhost:3000/"

def main_fun():
  r = requests.get(f'{BASE_URL}items/pokemons')
  return r.text


r = main_fun()
print(r)
