#include <stdio.h>
#include <stdlib.h>

int main(void){

	printf("Portas TCP abertas\n");
	system("netstat -nlpt");

	return 0;
}
