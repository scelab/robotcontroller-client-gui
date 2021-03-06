import socket

class MyClient(object):

    def __init__(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip, port):
        self.conn.connect((ip, port))

    def close(self):
        self.conn.shutdown(1)
        self.conn.close()

    def read(self):
        size = self.__read_size()
        return self.__read_data(size)

    def write(self, data):
        size = len(data)
        self.conn.send(size.to_bytes(4, byteorder='big'))
        self.conn.send(data)

    def __read_size(self):
        b_size = self.conn.recv(4)
        return int.from_bytes(b_size, byteorder='big')

    def __read_data(self, size):
        chunks = []
        bytes_recved = 0
        while bytes_recved < size:
            chunk = self.conn.recv(size - bytes_recved)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recved += len(chunk)
        return b''.join(chunks)

