#!/usr/bin/python3.6
# *-- coding: utf-8 --*

from Storage.StorageModule import StorageModule

class CloudStorage(StorageModule):

	#
	# Constructor
	#
	def __init__(self):
		# Inicialitzem el nom de la base de dades
		self.accessData['database'] = 'cloudStorage'

	#
	# Check data operations
	#

	def nodeExists(self, NodeName):
		cursor = self.__database.cursor()

		cursor.execute("SELECT * FROM NodeList WHERE NodeName IN ('%s')" % NodeName)

		# Get Node
		node = cursor.fetchone()

		cursor.close()

		return (node is not None);

	def nodeTypeExists(self, NodeName):
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
		if self.nodeExists(NodeName):
			raise Exception("Node %s already exists!", NodeName)

		# Check if 'NodeType' existes
		if not self.nodeTypeExists(NodeType):
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
		if self.nodeTypeExists(NodeType):
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
		if not self.nodeExists(NodeName):
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