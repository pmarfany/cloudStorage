#!/usr/bin/python3.6
# *-- coding: utf-8 --*

import mysql.connector
from mysql.connector import errorcode

class StorageModule:

	# Database access data
	accessData = {
		'user': 'ptin2017',
		'password': 'ptin2017',
		'host': 'localhost',
		'database': None
	}

	# Database
	database = None

	def __init__(self):
		pass

	#
	# Default connection and close operations
	#

	def connect(self):
		try:
			# He establish a connection with the database
			self.database = mysql.connector.connect(**self.accessData)

		# We handle some of the errors that may occur
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("ERROR: Bad username or password!")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("ERROR: Database does not exist!")
			elif err.errno == errorcode.CR_CONN_HOST_ERROR:
				print("ERROR: Cannot connect to database!")
			else:
				print(err)

	def close(self):
		# We close the database (if it's opened)
		if self.database is not None:
			self.database.close()
