#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main(int argc, char *argv[]){

	if(argc < 2 ){
		printf("======================================\n");
		printf("============= Modo de uso ============\n");
		printf("==     ./portscan 192.168.1.24      ==\n");
		printf("======================================\n");
	} else {
		int mySocket;
		int myConnect;

		int maxPort = 65535;
		int port;
		char *host = argv[1];

		struct sockaddr_in target;

		for( port = 0; port < maxPort; port++ ){

			mySocket = socket(AF_INET, SOCK_STREAM, 0);

			target.sin_family = AF_INET;
			target.sin_port = htons(port);
			target.sin_addr.s_addr = inet_addr(host);

			myConnect = connect(mySocket, (struct sockaddr *)&target, sizeof target);

			if(myConnect == 0){
				printf("Porta %d aberta\n", port);
				close(myConnect);
				close(mySocket);
				
			} else {
				close(myConnect);
				close(mySocket);
				
			}
		}
	}

	return 0;
}
