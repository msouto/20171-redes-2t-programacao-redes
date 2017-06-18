#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Código python3 para autenticação no SUAP/IFRN. Exemplo de como obter o token para a aplicação.

Prof. Moisés Souto - moises.souto@ifrn.edu.br
Clemente Junior - clemente.ferreira@academico.ifrn.edu.br

O token/ficha e a autorização devem ser obtidos, separadamente, em

    https://suap.ifrn.edu.br/api/docs/

    A url de requisições é: https://suap.ifrn.edu.br/api/v2/
'''

import requests
import json

def get_suap_token(username: str, password: str) -> str:
    token = 'token'
    resp = requests.post('https://suap.ifrn.edu.br/api/v2/autenticacao/token/?format=json',json={'username': username, 'password': password})
    payload = resp.json()
    print(payload)
    if token in payload.keys():
        return payload[token]
    return ''

if __name__ == '__main__':
    username = input("Digite sua matricula:")
    senha = input("Digite sua senha:")
    get_suap_token(username,senha)
