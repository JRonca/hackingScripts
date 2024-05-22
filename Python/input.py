#!/usr/bin/python
ip = input("Digite o IP: ")
port = int(input("Digite a porta: "))
ver = float(input("Digite a versao: "))

print("Scan version %.1f" %ver)
print("Scanning Host: %s on port: %d" %(ip,port))

print("IP -", type(ip))
print("Port -", type(port))
print("Version -", type(ver))