#include <stdio.h>

int main(void){
	char text[10];

	printf("MR Ronca\n");
	printf("Digite o texto: \n");
	fgets(text,10,stdin); // impede que se envie mais caracteres que o desejado
	printf("O texto digitado foi: %s\n", text);

	return 0;
}
