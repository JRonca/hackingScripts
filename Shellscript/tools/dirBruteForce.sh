#!/bin/bash
for word in $(cat lista.txt);
do
	resposta=$(curl -s -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" -o /dev/null -w "%{http_code}" $1/$word/)
	if [ $resposta == "200" ]
	then
		echo "Diretorio encontrado $1/$word"
	fi
done
