import json
arq = open('books.json')
txt = json.load(arq)

for item in txt['book']:
    print('Autor: ', item['author'])
