#!/usr/bin/python3.6
# *-- coding: utf-8 --*

import mysql.connector;
from mysql.connector import errorcode

class CloudStorage:

	# Database access data
	__accessData = {
		'user': 'ptin2017',
		'password': 'ptin2017',
		'host': 'localhost',
		'database': 'cloudStorage'
	}

	# Database
	__database = None;

	def __init__(self):
		pass;

	def connect(self):
		try:
			# He establish a connection with the database
			self.__database = mysql.connector.connect(**self.__accessData)

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
		# We close the database (if we opened)
		if self.__database is not None:
			self.__database.close()

	def createTable(self):
		# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
		pass

	def printListOfNodeTypes(self):
		cursor = self.__database.cursor()

		list = ("SELECT * FROM NodeType ORDER BY NodeID ASC")

		cursor.execute(list)

		for (NodeID, NodeName) in cursor:
			print("NodeID: {}, NodeName: {}".format(NodeID, NodeName.decode()))

		cursor.close()

	def printListOfNodes(self):
		cursor = self.__database.cursor()

		list = ("SELECT * FROM NodeList ORDER BY ID ASC")

		cursor.execute(list)

		for (Null, NodeID, NodeName) in cursor:
			print("NodeID: {}, NodeName: {}".format(NodeID, NodeName.decode()))

		cursor.close()

# Main program

cloud = CloudStorage()

cloud.connect()

cloud.getListOfNodeTypes()

cloud.close()
