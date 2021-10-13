import socket

s = socket.socket()

s.connect(("localhost", 6989))

fileName = input("Enter a file name: ")

s.send(fileName.encode())
content = s.recv(1024)
print(content.decode())

s.close()
