import socket

#Variaveis de apoio
HOST = '10.25.3.230'
#HOST = socket.gethostbyname('localhost')
PORT = 2000

#Instanciando transporte TCP/IP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associacao de porta ao processo servidor
tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen()



while True:
	client, addr = tcp_server_socket.accept()
	while True:
		#Recebe os dados do cliente
		data  = client.recv(1024)
		#Preparo mensagem de confirmacao de recebimento
		message = "Recebido"
		byte_msg = message.encode('utf_8')
		#Envio da mensagem de confirmacao
		client.send(byte_msg)

		if not data: break
		print("\n IP:",addr)
		print(" Mensagem recebida:", data)


client.close()
tcp_server_socket.close()
