#!/bin/bash
RED="\e[1;31m"
YELLOW="\e[1;33m"
GREEN="\e[1;32m"
BLUE="\e[1;34m"
RESET="\e[1;0m"
if [ "$1" == "" ]
then
        echo -e "$BLUE =============================================== $RESET"
        echo -e "$GREEN              JRONCA - PARSING HTML              $RESET"
        echo -e "$BLUE =============================================== $RESET"
        echo -e "$YELLOW                   MODO DE USO:              $RESET"
        echo -e "$RED              $0 SITE              $RESET"
        echo -e "$YELLOW                     Exemplo:              $RESET"
        echo -e "$RED           $0 globo.com              $RESET"
        echo -e "$BLUE =============================================== $RESET"
else
	wget $1
	cat index.html | grep "href=" > index.txt
	sed -i 's/href="/$/' index.txt;
	cat index.txt | cut -d "$" -f 2 | cut -d "\"" -f 1 | grep "http" | cut -d "/" -f 3 > lista.txt
	rm index.*
	for url in $(cat lista.txt | sort -u)
	do
		host $url | grep "has address"
	done
	rm lista.txt
fi
