#!/usr/bin/python3.6
# *-- coding: utf-8 --*

import mysql.connector
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

	#
	# Default connection and close operations
	#

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
		# We close the database (if it's opened)
		if self.__database is not None:
			self.__database.close()

	#
	# Check data operations
	#

	def __nodeExists(self, NodeName):
		cursor = self.__database.cursor()

		cursor.execute("SELECT * FROM NodeList WHERE NodeName IN ('%s')" % NodeName)

		# Get Node
		node = cursor.fetchone()

		cursor.close()

		return (node is not None);

	def __nodeTypeExists(self, NodeName):
		cursor = self.__database.cursor()

		cursor.execute("SELECT * FROM NodeType WHERE NodeName IN ('%s')" % NodeName)

		# Get Node
		node = cursor.fetchone()

		cursor.close()

		return (node is not None);

	#
	# Insert data operations
	#

	def addNode(self, NodeName, NodeType):
		# Create database cursor
		cursor = self.__database.cursor()

		# Check if 'NodeName' exists
		if self.__nodeExists(NodeName):
			raise Exception("Node %s already exists!", NodeName)

		# Check if 'NodeType' existes
		if not self.__nodeTypeExists(NodeType):
			raise Exception("NodeType %s does not exist!", NodeType)

		# Database OP strings
		selectID = "SELECT NodeID FROM NodeType WHERE NodeName = '%s'" % NodeType
		addnode = "INSERT INTO NodeList VALUES (DEFAULT, '%s', (%s))" % (NodeName, selectID)

		# Execute command
		cursor.execute(addnode)

		# Commit changes
		self.__database.commit()

		# Close database cursor
		cursor.close()

	def addNodeType(self, NodeType):
		# Create database cursor
		cursor = self.__database.cursor()

		# Check if 'NodeType' existes
		if self.__nodeTypeExists(NodeType):
			raise Exception("NodeType %s already exists!", NodeType)

		# Database OP strings
		addnodetype = "INSERT INTO NodeType VALUES (DEFAULT, '%s')" % NodeType

		# Execute command
		cursor.execute(addnodetype)

		# Commit changes
		self.__database.commit()

		# Close database cursor
		cursor.close()

	def addEvent(self, NodeName, EventInfo):
		# Create database cursor
		cursor = self.__database.cursor()

		# Check if 'NodeName' exists
		if not self.__nodeExists(NodeName):
			raise Exception("Node %s does not exist!", NodeName)

		# Database OP strings
		selectID = "SELECT ID FROM NodeList WHERE NodeName = '%s'" % NodeName
		addevent = "INSERT INTO EventList VALUES (DEFAULT, (%s), '%s', DEFAULT)" % (selectID, EventInfo)

		# Execute command
		cursor.execute(addevent)

		# Commit changes
		self.__database.commit()

		# Close database cursor
		cursor.close()

	#
	# Print operations
	#

	def printNodeList(self):
		cursor = self.__database.cursor()

		list = ("SELECT * FROM NodeList ORDER BY ID ASC")

		cursor.execute(list)

		for (NodeID, NodeName, NodeType) in cursor:
			print("NodeID: {}, NodeName: {}, NodeType: {}".format(NodeID, NodeName.decode(), NodeType))

		cursor.close()

	def printNodeTypes(self):
		cursor = self.__database.cursor()

		list = ("SELECT * FROM NodeType ORDER BY NodeID ASC")

		cursor.execute(list)

		for (NodeID, NodeName) in cursor:
			print("NodeID: {}, NodeName: {}".format(NodeID, NodeName.decode()))

		cursor.close()

	def printEventList(self):
		cursor = self.__database.cursor()

		list = ("SELECT * FROM EventList ORDER BY TimeStamp ASC")

		cursor.execute(list)

		for (NodeID, NodeName, EventInfo, TimeStamp) in cursor:
			print("NodeID: {}, NodeName: {}, EventInfo: {}, TimeStamp: {}".format(NodeID, NodeName, EventInfo.decode(), TimeStamp))

		cursor.close()