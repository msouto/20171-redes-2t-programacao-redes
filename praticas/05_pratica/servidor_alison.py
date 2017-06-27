from math import sqrt
import socket
serverHost = 'localhost'
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))

while True:
	message, clienAddress = serverSocket.recvfrom(2048)
	message = message.decode("utf-8")
	message_div = message.split(" ")
	if message_div[0] == "sair":
		break
	else:
		if message_div[0] == "soma":
			validade = len(message_div)
			if validade == 4:
				soma = int(message_div[1]) + int(message_div[2])
				soma = str(soma)
				soma = soma.encode("utf-8")
				serverSocket.sendto(soma, clienAddress)
			else:
				message1 = "Mensagem invalida"
				message1 = message1.encode("utf-8")
				serverSocket.sendto(message1, clienAddress)
		elif message_div[0] == "raiz_quadrada":
			validade = len(message_div)
			if validade == 3:
				raiz = sqrt(int(message_div[1]))
				raiz = str(raiz)
				raiz = raiz.encode("utf-8")
				serverSocket.sendto(raiz, clienAddress)
			else:
				message1 = "Mensagem invalida"
				message1 = message1.encode("utf-8")
				serverSocket.sendto(message1, clienAddress)
		else:
			message1 = "Mensagem invalida"
			message1 = message1.encode("utf-8")
			serverSocket.sendto(message1, clienAddress)

serverSocket.close()
