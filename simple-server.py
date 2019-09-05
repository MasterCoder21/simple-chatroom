import sys
import select
import socket
from thread import *

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print "Usage: simple-server HOST PORT"
    exit()

Host = str(sys.argv[1])
Port = int(sys.argv[2])
Server.bind((Host, Port))
Server.listen(100)
ListOfClients = []

def Clientthread(Conn, Addr):
    Conn.send("Welcome to my simple chatroom!")
    while True:
            try:
                Message = Conn.recv(2048)
                if Message:
                    print "[" + Addr[0] + "] " + Message
                    MessageToSend = "[" + Addr[0] + "] " + Message
                    Broadcast(MessageToSend, Conn)

                else:
                    Remove(Conn)
            except:
                continue

def Broadcast(Message, Connection):
    for Clients in ListOfClients:
        if Clients != Connection:
            try:
                Clients.send(Message)
            except:
                Clients.close()
                Remove(Clients)

def Remove(Connection):
    if Connection in ListOfClients:
        ListOfClients.remove(Connection)

while True:
    Conn, Addr = Server.accept()
    ListOfClients.append(Conn)
    print Addr[0] + " connected"
    StartNewThread(ClientThread, (Conn, Addr))

Conn.close()
Server.close()
