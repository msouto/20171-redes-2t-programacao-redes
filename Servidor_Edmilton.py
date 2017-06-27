import socket
from math import sqrt
import os

def calcSoma(a, b):
    c = float(a) + float(b)
    return str(c)

def calcRaiz(a):
    return str(sqrt(float(a)))

def operCalc(operacao):
    lOperacao = operacao.split()
    if lOperacao[0].upper() == 'SOMA':
        if len(lOperacao) == 3:
            if lOperacao[1].isnumeric() and lOperacao[2].isnumeric():
                print(len(lOperacao))
                return calcSoma(lOperacao[1], lOperacao[2])
            else:
                sErro = 'Os valores passados não são numéricos.'
                return sErro
        else:
            sErro = 'Não há parâmetros suficiente para realizar a operação \'soma\'.'
            return sErro
    elif lOperacao[0].upper() == 'RAIZ':
        if lOperacao[1].isnumeric():
            return calcRaiz(lOperacao[1])
        else:
            sErro = 'Os valores passados não são numéricos.'
            return sErro
    else:
        sErro = 'Mensagem inválida'
        return sErro


os.system('cls' if os.name == 'nt' else 'clear')
serverHost = 'localhost'
serverPort = 3600

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))

print("Servidor Iniciado.")

while True:
    try:
        strComandos, clientAddress = serverSocket.recvfrom(2048)
        print('Conexão iniciada por: ', clientAddress)
        lComandos = strComandos.decode('utf-8').rstrip('\n').split('\n')
        result = ''
        print(lComandos)
        for comOper in lComandos:
            result += 'Comando \'' + comOper + '\' Resultado: ' + operCalc(comOper) + '\n'
        print(result)
        serverSocket.sendto(result.encode(), clientAddress)
        serverSocket.close()
        break
    except:
        result = 'Houve um erro na execução dos comandos. Favor tentar novamente.'
        print(result)
        serverSocket.sendto(result.encode(), clientAddress)