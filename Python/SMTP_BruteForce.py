#!/usr/bin/python

import socket,sys,re
import sys

if (len(sys.argv) != 3):
        print("Modo de uso: ",sys.argv[0],"IP fileuser")
        sys.exit(0)


ip = sys.argv[1]
file = open(sys.argv[2])
port = 25

print("Users encontrados")

for user in file:
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.connect((ip,port))

        banner = tcp.recv(1024)

        tcp.send(str.encode("VRFY " + user))
        user = tcp.recv(1024).decode('utf-8')

        if re.search("252", user):
                print(user.strip("252 2.0.0"))