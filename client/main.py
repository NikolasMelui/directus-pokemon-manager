import requests

BASE_URL = "https://loocalhost:3000/"


def main_fun():
  r = requests.get(BASE_URL)
  return r.text


r = main_fun()
print(r)
