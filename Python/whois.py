import socket
import sys

port = 43

iana = "whois.iana.org"

host = sys.argv[1]

ianaSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ianaSocket.connect((iana, port))

print("______________________________________")
print("IANA")
print("______________________________________")

ianaSocket.send(str.encode(host + "\r\n"))

ianaReturn = ianaSocket.recv(1024).decode('latin-1').strip()
print(ianaReturn)
print("______________________________________")

ianaReturn = ianaReturn.split()

refer = ianaReturn[ianaReturn.index('refer:') + 1]

referSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
referSocket.connect((refer, port))


print(refer)
print("______________________________________")

referSocket.send(str.encode(host + "\r\n"))

referReturn = referSocket.recv(1024).decode('latin-1').strip()
print(referReturn)
print("______________________________________")

ianaSocket.close()
referSocket.close()