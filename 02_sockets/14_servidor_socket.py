import socket

#Variaveis de apoio
#HOST = socket.gethostbyname('localhost')
HOST = '10.25.3.230'
PORT = 2000

#instanciando transporte TCP/IP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#associacao de porta ao processo servidor
tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen()

client, addr = tcp_server_socket.accept()
while True:
    #receber os dados do cliente
    data = client.recv(1024)
    #preparo mensagem de confirmacao de recebimento
    message = "Recebido"
    byte_msg = message.encode('utf-8')
    #envio da mensagem de confirmacao
    client.send(byte_msg)
    if not data: break
    print("\n IP:",addr)
    print(" Mensagem recebida:", data)

client.close()
tcp_server_socket.close()
