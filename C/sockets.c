#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main(void){
	int mySocket;
	int myConnect;

	struct sockaddr_in target;

	mySocket = socket(AF_INET, SOCK_STREAM, 0);

	target.sin_family = AF_INET;
	target.sin_port = htons(80);
	target.sin_addr.s_addr = inet_addr("192.168.100.1");

	myConnect = connect(mySocket, (struct sockaddr *)&target, sizeof target);

	if(myConnect == 0){
		printf("Porta aberta\n");
		close(mySocket);
		close(myConnect);
	} else {
		printf("Porta fechada\n");
		close(mySocket);
		close(myConnect);
	}

	return 0;
}
