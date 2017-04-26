#programa com função que trata data por extenso
def data_por_extenso(texto):
    meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    data_num = texto.split('/')
    return data_num[0] + ' de ' + meses[int(data_num[1])-1] + ' de ' + data_num[2]

print(data_por_extenso('01/01/1970'))
print(data_por_extenso('01/06/2016'))
