import socket

Socket = socket.socket()
Host = socket.gethostname()
Port = 1337

Socket.connect((Host, Port))
print Socket.recv(1024)
Socket.close()
