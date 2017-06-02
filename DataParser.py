from CloudStorage import CloudStorage
import json

## DataParser
class DataParser:

	__cloudStorage = None;

	# Inicialització
	def __init__(self, storage: CloudStorage):
		self.__cloudStorage = storage

	# Llegim el missatge i el guardem
	def decodeAndStorage(self, data):
		# Decode JSON data
		jdata = json.loads(data.decode('utf-8'))

		# Creem les estructures a la BD
		self.__decode(jdata)

		# Afegim la línia d'esdeveniments
		self.__cloudStorage.addEvent(jdata['id'], data)

	# Decodificar el missatge
	def __decode(self, data):
		# Obtenir "id" amb JSON de data
		identificador = data['id']

		# Comprovar si NO existeix
		if not self.__cloudStorage.nodeExists(identificador):

			# ¿¿Obtenir tipus?? - igual amb un switch "cutre" en plan:
				# si "semaforo_n" es Sempahore.
				# si "SmartCityApp" (aplicació mòbil), doncs, per exemple, "SmartCityApp".
			#### linia de codi

			# Comprovar si NO existeix el tipus
			if not self.__cloudStorage.nodeTypeExists(tipus):
				# Creem el tipus
				self.__cloudStorage.addNodeType(tipus)

			# JA EXISTEIX EL TIPUS (sinó existia abans, l'acabem de crear)
			# Creem el node
			self.__cloudStorage.addNode(identificador, tipus)
