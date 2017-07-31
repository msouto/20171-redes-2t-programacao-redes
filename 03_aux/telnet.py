# telnet program example
import socket, select, string, sys

#main function
if __name__ == "__main__":

    if(len(sys.argv) < 3) :
        print('Usage : python telnet.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()

    print('Connected to remote host')

    while 1:

        # The socket list contains 2 sockets. First is the sys.stdin which is stream for standard input or the user input at the command line. The other one is the socket that is connected to remote server. The select function keeps listening on both of them. It is a blocking function and returns if either of the 2 things happens
        #
        # 1. Server sends a message
        # 2. User hits enter after typing in a message
        # If the server socket is ready to be read, then just call recv function on it. If the user input is ready to be read then call sys.stdin.readline() function get the user message. Thats all about it.
        #
        # The telnet client shown above is a minimal one. The actual telnet client has lots of other features which you can try to implement. The above telnet client can be used as a terminal chat client as well with little modifications. Just have to write a chat server. Will come up with a post on that soon.
        #
        # Note
        #
        # The above shown program will work only on linux and not on windows. The program uses the select function read the command line input (stdin). On windows the select function cannot read file descriptors. It can only read sockets created inside winsock. The python documentation on select function mentions this

        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print('Connection closed')
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)

            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
