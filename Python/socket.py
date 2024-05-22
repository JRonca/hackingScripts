#!/usr/bin/python
import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

res = mySocket.connect_ex((ip, port))

if (res == 0):
    print("Porta aberta")
else:
    print("Porta fechada")