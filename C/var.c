#include <stdio.h>

int main(void){
	int porta = 80;
	char ip[] = "192.168.0.1";
	float ver = 1.1;

	printf("MR Ronca\n");
	printf("Scan Porta: %d\n", porta);
	printf("Scan IP: %s\n", ip);
	printf("Scan version: %.1f\n", ver);

	return 0;
}
