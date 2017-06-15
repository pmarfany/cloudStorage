#!/usr/bin/python3.6
# *-- coding: utf-8 --*

import json
from Storage.loginStorage import loginStorage

# ParserModule
class loginParser:

	__loginStorage = None;

	STATUS = 'Status'
	STATUS_LOGIN = 'Login'
	STATUS_SIGNUP = 'SignUp'

	STATUS_OK = 'OK'
	STATUS_NO = 'NO'

	MESSAGE_NAME = 'Name'
	MESSAGE_SURNAME = 'Surname'
	MESSAGE_EMAIL = 'Email'
	MESSAGE_PASSWORD = 'Password'

	# Inicialització
	def __init__(self, storage: loginStorage):
		self.__loginStorage = storage

	# Decodificar el missatge
	def decodeAndStorage(self, data):
		# Decode JSON data
		message = json.loads(data.decode('utf-8'))
		print("Received data: " + data.decode('utf-8'))

		# Check or register user
		if message[self.STATUS] == self.STATUS_LOGIN:
			return self.__loginStorage.login(message[self.MESSAGE_EMAIL],
														message[self.MESSAGE_PASSWORD])

		elif message[self.STATUS] == self.STATUS_SIGNUP:
			return self.__loginStorage.register(message[self.MESSAGE_NAME], message[self.MESSAGE_SURNAME],
														message[self.MESSAGE_EMAIL], message[self.MESSAGE_PASSWORD])

		else:
			return False

	def OKpacket(self):
		return self.__ACKpacket(self.STATUS_OK)

	def NOpacket(self):
		return self.__ACKpacket(self.STATUS_NO)

	def __ACKpacket(self, status):
		# We create & return the packet
		data = { self.STATUS : status }
		return json.dumps(data)