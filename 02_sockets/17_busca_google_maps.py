#!/usr/bin/env python3

from pygeocoder import Geocoder
if __name__ == '__main__':
    endereco='Av. Senador Salgado Filho, 1559, Natal, RN'
    print(Geocoder.geocode(endereco)[0].coordinates)
