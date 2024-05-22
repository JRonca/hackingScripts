#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>

// man gethostbyname
// man inet

int main (int argc, char *argv[]){
    if(argc <= 1){
		printf("Modo de uso: ./dns_resolver businesscorp.com.br\n");
	}else{
		struct hostent *alvo = gethostbyname(argv[1]);
		//man gethostbyname
		if(alvo == NULL){
			printf("ERRO - Alvo nao encontrado!\n");
		}else{
			printf("IP: %s\n",inet_ntoa(*((struct in_addr *)alvo->h_addr)));
			//man inet
		}
	}
	return 0;
}
