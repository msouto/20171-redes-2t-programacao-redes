import json

f=open('pratica.json')
e=json.load(f)

b=e['book']
l1=b[0]
l2=b[1]

autores=[l1['author'],l2['author']]

print(autores)

