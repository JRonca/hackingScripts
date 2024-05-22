#!/usr/bin/python
import socket
import sys

ip = sys.argv[1]

for port in range(1,65535) :
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = mySocket.connect_ex((ip, port))
    if (res == 0):
        print("Porta", port,"[ABERTA]")
        mySocket.close()