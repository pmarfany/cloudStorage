import socket

## CLOUD
class ServerSocket:

	SEND_SIZE = 1024

	s = None
	conn = None
	addr = None

	def __init__(self, host, port):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((host, port))
		self.s.listen(5)

	def s_accept(self):
		self.conn, self.addr = self.s.accept()

	def send_data(self,content):
		self.conn.send(content.encode())

	def read_data(self):
		buf = self.conn.recv(self.SEND_SIZE)
		return buf

	def close_socket(self):
		self.conn.close()

