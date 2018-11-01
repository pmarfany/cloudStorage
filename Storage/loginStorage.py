#!/usr/bin/python3.6
# *-- coding: utf-8 --*

from Storage.StorageModule import StorageModule

class loginStorage(StorageModule):

	#
	# Constructor
	#
	def __init__(self):
		# Inicialitzem el nom de la base de dades
		self.accessData['database'] = 'userLogin'

	#
	# Funció de login
	# Comprova que l'usuari existeixi i que el password correspongui.
	#
	def login(self, email, password):
		# Create database cursor
		cursor = self.database.cursor()

		# Check if user exists
		state = self.__userExists(email)
		if not state: return False

		# Check if password matches
		checkUser = "SELECT * FROM userList WHERE email IN ('%s') AND password IN ('%s')" % (email, password)
		cursor.execute(checkUser)

		# Get login
		login = cursor.fetchone()

		cursor.close()

		return (login is not None)

	#
	# Funció de register
	# Comprova que l'usuari no existeixi i el crea.
	#
	def register(self, name, surname, email, password):
		# Create database cursor
		cursor = self.database.cursor()

		# Check if user exists
		state = self.__userExists(email)
		if state: return False

		# Add User
		addUser = "INSERT INTO userList VALUES (DEFAULT, ('%s'), ('%s'), ('%s'), ('%s'))" % (name, surname, email, password)
		cursor.execute(addUser)

		# Commit changes
		self.database.commit()

		cursor.close()

		return True

	#
	# Funció de comprovació d'usuari
	# Comprova que l'usuari existeixi.
	#
	def __userExists(self, email):
		# Create database cursor
		cursor = self.database.cursor()

		# Check if user exists
		cursor.execute("SELECT * FROM userList WHERE email IN ('%s')" % email)

		# Get user
		user = cursor.fetchone()

		cursor.close()

		return (user is not None);
