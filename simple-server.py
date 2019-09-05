#!/usr/bin/python
import socket

Socket = socket.socket()
Host = socket.gethostname()
Port = 1337
Socket.bind((Host, Port))

Socket.listen(5)

while True:
	Connection, Address = Socket.accept()
	print 'Got stinky connection from', Address
	Connection.send('you stinky disconnect from me nerd')
	Connection.close()
