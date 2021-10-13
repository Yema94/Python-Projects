import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

print("Server listening on port : ", port)
s.listen(1)

connection_obj, client_address =  s.accept()

print("Connection from : ", str(client_address))

connection_obj.send(b"Hello, How are you?")
connection_obj.send("bye".encode())
connection_obj.close()