import socket

host = 'localhost'
port = 6989

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

print("Server listening on port : ", port)
s.listen(1)

connection_obj, client_address =  s.accept()

fileName = connection_obj.recv(1024)
try:
    f = open(fileName, "rb")
    content = f.read()
    connection_obj.send(content)
    f.close()
except FileNotFoundError:
    connection_obj.send(b"File does not exist")

connection_obj.close()