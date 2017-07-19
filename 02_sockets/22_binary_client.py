import socket

HOST = "localhost"
PORT = 8051
# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# attempt to connect to host
sock.connect((HOST,PORT))

while 1:
	message = input("Your Message: ")
	sock.send(bytes(message,'UTF-8'))
	if (message == 'o'):
		with open('test1.png', 'wb+') as output:
			rec = sock.recv(10240)
			output.write(rec)

	elif (message == 'q'):
		break

sock.close()
