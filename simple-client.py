import sys
import select
import socket

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print "Usage: simple-client HOST PORT"
    exit()

Host = str(sys.argv[1])
Port = int(sys.argv[2])
Server.connect((Host, Port))

while True:
    SocketsList = [sys.stdin, Server]
    ReadSockets, WriteSocket, ErrorSocket = select.select(SocketsList, [], [])
    for Socks in ReadSockets:
        if Socks == Server:
            Message = Socks.recv(2048)
            print Message
        else:
            Message = sys.stdin.readline()
            Server.send(Message)
            sys.stdout.write("[You] ")
            sys.stdout.write(Message)
            sys.stdout.flush()
server.close()
