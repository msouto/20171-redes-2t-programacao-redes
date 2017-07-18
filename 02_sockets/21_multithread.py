import socket
import threading

class ThreadServer(object):

    #construtor da classe
    def __init__(self, host, port):
        self.host = host #passando por parametro
        self.port = port #passando por parametro
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #descritor do socket
        #liberando o reuso das portas
        #caso contrario, o sistema diria que a porta esta em uso
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            #Start uma thread
            threading.Thread(target = self.listenToClient, args = (client,address) ).start()


    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    #configurar para enviar o echo de volta o dado recebido
                    response = data
                    client.send(response)
                else:
                    raise error('Cliente desconectado')
            except:
                client.close()
                return False

if __name__ == '__main__':
    while True:
        port_num = input("Porta:")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadServer('localhost',port_num).listen()
