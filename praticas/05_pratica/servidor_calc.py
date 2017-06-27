import socket

HOST = ''
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)


while True:
	
	aux, cliente = udp.recvfrom(1024)
	
	if aux == '1':
		aux2, cliente = udp.recvfrom(1024)
		aux3, cliente = udp.recvfrom(1024)
		print 'Soma = ', int(aux2)+int(aux3)
	elif aux == '2':
		aux4, cliente = udp.recvfrom(1024)
		print 'Raiz quadrada eh: ', int(aux4) ** 2
	else:
		print 'Dado desconhecido'
		break
	
udp.close()
