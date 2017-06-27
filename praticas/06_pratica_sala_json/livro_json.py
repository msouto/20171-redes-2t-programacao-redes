import json

arq = open('arq_json.json', 'rb')
dados = json.load(arq)

for item in (dados['book']):
	print('Autor: => ', item['author'])