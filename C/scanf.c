#include <stdio.h>

int main(void){
	int porta;
	char ip[16];

	printf("MR Ronca\n");
	printf("Digite o IP: \n");
	scanf("%s", &ip);
	printf("Digite a porta: \n");
	scanf("%d", &porta);

	printf("Varrendo o host %s na porta %d\n", ip, porta);

	return 0;
}
