import socket
HOST = socket.gethostbyname('localhost')
PORT = 2000

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Estrutura inicial do client TCP/IP
tcp_client_socket.connect((HOST,PORT))

#preparando menssagem
message = "Hello World"
byte_msg = message.encode('utf_8')

tcp_client_socket.send(byte_msg)
data = tcp_client_socket.recv(1024)
tcp_client_socket.close
print("MSG recebida:", repr(data))
