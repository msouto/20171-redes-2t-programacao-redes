import socket

#Variaveis de apoio
HOST = socket.gethostbyname('localhost')
PORT = 2000

#instanciando transporte TCP/IP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#associacao de porta ao processo servidor
tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen()
