#!/usr/bin/python
import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((ip, port))
banner = mySocket.recv(1024)

print(banner)