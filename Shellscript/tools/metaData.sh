#!/bin/bash
if [ "$2" == "" ]
then
	echo "========================================================="
	echo "=================      Script Use      =================="
	echo "========================================================="
	echo "  $0 sitedesejado.com pdf"
	echo "========================================================="
else

	siteList=$(lynx --dump "https://google.com/search?&q=site:$1+ext:$2" | grep ".$2" | cut -d = -f2 | grep -E -v "site|google" | sed 's/...$//')

	for link in $siteList
	do
		wget -q $link
	done
	exiftool *.pdf
	rm *.pdf
fi
