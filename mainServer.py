#!/usr/bin/python3.6
# *-- coding: utf-8 --*

import sys
from ServerSocket import ServerSocket
from CloudStorage import CloudStorage

# Default data
serverName = '192.168.1.46'
serverPort = 10000

# Optional server name argument
if (len(sys.argv) > 1):
	serverName = sys.argv[1]

# Optional server port number
if (len(sys.argv) > 2):
	serverPort = int(sys.argv[2])

# Creem un 'serverSocket'
socket = ServerSocket(serverName, serverPort)

# Creem un objecte de la classe 'CloudStorage
cloudStorage = CloudStorage()

cloudStorage.connect()

# Bucle infinit
while True:
	# Connectar socket
	socket.s_accept()

	# Get dades
	print(socket.read_data())

	# 'Parse' dades
	# cloudStorage.addNode("NodeName", "NodeType")
	# cloudStorage.addNodeType("NodeType")
	# cloudStorage.addEvent("NodeName", "EventInfo")
	# ...

	# Enviar resposta
	socket.send_data("Recibido!")

	# Tancar socket
	socket.close_socket()

cloudStorage.close()