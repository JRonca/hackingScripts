#!/usr/bin/python
ip = "192.168.1.1"
port = 80
ver = 1.1
booleanTest = True

print("Scan version", ver)
print("Scanning Host:", ip, "on port", port)

print("IP -", type(ip))
print("Port -", type(port))
print("Version -", type(ver))
print("Bool -", type(booleanTest))

print("Scan version %.1f" %ver)
print("Scanning Host: %s on port: %d" %(ip,port))
print("This ticket are %r" %booleanTest)
