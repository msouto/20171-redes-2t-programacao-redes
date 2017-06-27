import socket
import os

HOST = '127.0.0.1'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)


while True:
	print '===== SELECIONE A OPERACAO =====\n 1 - ADICAO\n 2 - RAIZ QUADRADA\n 5 - SAIR\n'
	
	aux = raw_input()
	udp.sendto (aux, dest)
	
	if aux == '1':
		print 'Digite dois valores para soma:\n'
		aux2 = raw_input()
		udp.sendto (aux2, dest)
		aux3 = raw_input()
		udp.sendto (aux3, dest)
		pass
	elif aux == '2':
		print 'Digite um valor para raiz:\n'
		aux4 = raw_input()
		udp.sendto (aux4, dest)
		pass
	elif aux == '5':
		os.system('cls' if os.name == 'nt' else 'clear')
		break
	else:
		print 'Opcao invalida!\n'

udp.close()
