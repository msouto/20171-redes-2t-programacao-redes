import socket
import os
serverName = 'localhost'
serverPort = 3600

os.system('cls' if os.name == 'nt' else 'clear')

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lComandos = ''
message = input('Insira a operação, o primeiro número e o segundo (se necessário): ')
while True:
    if message.upper() == 'SAIR':
        print('Saindo...')
        break
    if message.upper() != 'ENVIAR':
        lComandos += message + '\n'
        message = input('Próxima operação (\'Enviar\' para finalizar e enviar os comandos): ')
    else:
        byte_msg = lComandos.encode('utf-8')
        clientSocket.sendto(byte_msg, (serverName, serverPort))
        result, serverAddress = clientSocket.recvfrom(2048)
        print(result.decode('utf-8'))
        clientSocket.close()
        break