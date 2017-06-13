#!/usr/bin/env python3
import requests
import json

def geocode(address):
    parameters = {'address': address, 'sensor':'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    resposta = response.json()
    print(resposta['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('Av. Senador Salgado Filho, 1559, Natal, RN')
