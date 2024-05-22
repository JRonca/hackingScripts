#!/usr/bin/python
import socket
import sys

ip = sys.argv[1]
port = 21

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((ip, port))

banner = mySocket.recv(1024)
print(banner)

print("Enviando user")

mySocket.send(str.encode("USER admin\r\n"))

banner = mySocket.recv(1024)
print(banner)

print("Enviando senha")

mySocket.send(str.encode("PASS admin\r\n"))

banner = mySocket.recv(1024)
print(banner)