#!/usr/bin/python3.6
# *-- coding: utf-8 --*
import sys
from os import popen
from ServerSocket import ServerSocket
from CloudStorage import CloudStorage
from DataParser import DataParser

# Get my IPAddress
def getIPAddress():
    return popen('hostname -I').read().strip()

# Default data
serverName = getIPAddress()
serverPort = 10000

# Optional server name argument
if (len(sys.argv) > 1):
	serverName = sys.argv[1]

# Optional server port number
if (len(sys.argv) > 2):
	serverPort = int(sys.argv[2])

# Creem un 'serverSocket'
socket = ServerSocket(serverName, serverPort)

# Creem un objecte de la classe 'CloudStorage'
cloudStorage = CloudStorage()
cloudStorage.connect()

# Creem un objecte de la classe 'DataParser'
dataParser = DataParser(cloudStorage)

# Bucle infinit
while True:
	# Connectar socket
	socket.s_accept()

	# Get dades
	data = socket.read_data()

	# Parse dades
	DataParser.decodeAndStorage(data)

	# Tancar socket
	socket.close_socket()

cloudStorage.close()