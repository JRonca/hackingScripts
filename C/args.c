#include <stdio.h>

int main(int argc, char *argv[]){
    if(argc < 3){
        printf("Modo de uso: %s 192.168.1 80\n", argv[0]);
    } else {
        int i;
        char *porta;

        porta = argv[2];
        for(i = 1; i<=10; i++){
            printf("Varrendo Host %s.%d na Porta %s\n", argv[1], i, porta);
        }

        printf("Temos %d argumentos sendo enviados para o programa %s\n", argc-1, argv[0]);
    }

	return 0;
}
