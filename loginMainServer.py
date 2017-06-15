#!/usr/bin/python3.6
# *-- coding: utf-8 --*
import sys
from os import popen

from Storage.loginStorage import loginStorage
from Connection.ServerSocket import ServerSocket
from DataParser.loginParser import loginParser

# Get my IPAddress
def getIPAddress():
    return popen('hostname -I').read().strip()

# Default data
serverName = getIPAddress()
serverPort = 10001

# Optional server name argument
if (len(sys.argv) > 1):
	serverName = sys.argv[1]

# Optional server port number
if (len(sys.argv) > 2):
	serverPort = int(sys.argv[2])

# Creem un 'serverSocket'
socket = ServerSocket(serverName, serverPort)

# Creem un objecte de la classe 'loginStorage'
loginStorage = loginStorage()
loginStorage.connect()

# Creem un objecte de la classe 'DataParser'
loginParser = loginParser(loginStorage)

# Bucle infinit
while True:
	# Connectar socket
	socket.s_accept()

	# Get dades
	data = socket.read_data()

	# Parse dades
	result = loginParser.decodeAndStorage(data)

	# Send ACK or NACK
	if result:
		socket.send_data(loginParser.OKpacket())
		print("Response: OK")
	else:
		socket.send_data(loginParser.NOpacket())
		print("Response: NO")

	# Tancar socket
	socket.close_socket()

loginStorage.close()