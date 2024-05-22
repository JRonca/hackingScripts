#!/usr/bin/python

import socket
import sys

if (len(sys.argv) != 3):
    print("Modo de uso: ",sys.argv[0],"IP user")
    sys.exit(0)


ip = sys.argv[1]
port = 25

print("Conectando ao servidor...")

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((ip,port))

banner = tcp.recv(1024).decode('utf-8')

print(banner)

print("Testando User...")

tcp.send(str.encode("VRFY " + sys.argv[2] + "\r\n"))
user = tcp.recv(1024).decode('utf-8')

print(user)