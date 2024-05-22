#!/usr/bin/python
import sys
from scapy.all import *
import numpy as np

conf.verb = 0

pIP = IP(dst=sys.argv[1])

portas = [21,22,23,25,80,443,110]

pTCP = TCP(dport=portas, flags="S")

pacote = pIP/pTCP

resposta, noresp = sr(pacote)

for resp in resposta:
    porta = resp[1][TCP].sport
    flag = resp[1][TCP].flags
    if (flag == "SA"):
        print("Port ",porta, " OPEN")