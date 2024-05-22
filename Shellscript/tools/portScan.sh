#!/bin/bash
if [ "$1" == "" ]
then
	echo "JRonca - PORT SCAN"
	echo "Modo de uso: $0 REDE PORTA"
	echo "Exemplo: $0 192.168.0 80"
else
	for host in {1..254};
	do
		sudo hping3 -S -p $2 -c 1 $1.$host 2> /dev/null | grep "SA" | cut -d " " -f 2
	done
fi
