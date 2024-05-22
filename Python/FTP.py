#!/usr/bin/python

import socket
import sys

ip = sys.argv[1]
port = 21

if len(sys.argv) > 2:
    port = int(sys.argv[2])

print("Conectando ao servidor...")

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((ip,port))

banner = tcp.recv(1024)

print(banner)

print("Enviando User...")

tcp.send(str.encode("USER ftp\r\n"))
user = tcp.recv(1024)

print(user)

print("Enviando Pass...")

tcp.send(str.encode("PASS ftp\r\n"))
userPass = tcp.recv(1024)

print(userPass)

print("Enviando comando PWD...")

tcp.send(str.encode("pwd\r\n"))
cmd = tcp.recv(1024)

print(cmd)

print("Enviando comando HELP...")

tcp.send(str.encode("help\r\n"))
cmdHelp = tcp.recv(2048)

print(cmdHelp)