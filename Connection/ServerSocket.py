import socket

## CLOUD
class ServerSocket:

	SEND_SIZE = 2048

	s = None
	conn = None
	addr = None

	# Inicialitazió i connexió del servidor
	def __init__(self, host, port):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((host, port))
		self.s.listen(5)

	# Acceptar connexió del client
	def s_accept(self):
		self.conn, self.addr = self.s.accept()

	# Enviar dades
	def send_data(self, content):
		self.conn.send(content.encode())

	# Obtenir dades del buffer
	def read_data(self):
		buf = self.conn.recv(self.SEND_SIZE)
		return buf

	# Finalitzar conneció del servidor
	def close_socket(self):
		self.conn.close()

