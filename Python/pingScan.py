#!/usr/bin/python
import sys
sys.stderr = None
from scapy.all import *
import numpy as np

conf.verb = 0
net = sys.argv[1]

for host in range(1,255):
    ip = net + "." + str(host)
    conf.verb = 0
    pIP = IP(dst=ip)
    pacote = pIP/ICMP()
    resp, noresp = sr(pacote, timeout=1)
    #print(resp[0][1][IP].src)
    for resposta in resp:
        print(resposta[1][IP].src)