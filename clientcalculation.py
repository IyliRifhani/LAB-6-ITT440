CLIENT CALCULATION

import socket
import signal
import sys

ClientSocket = socket.socket()
host = '192.168.56.106'
port = 8828

print('Waiting for the connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    Input = input('Please Enter the operation and number: ')

    if Input == 'exit':
        break
    else:
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

ClientSocket.close()

