#include <stdio.h>

int main(){
    int salario;
    printf("Qual o seu salario? ");
    scanf("%d", &salario);

    if (salario <= 1500){
        printf("Sal�rio baixo");
    }
    else if (salario <= 2000){
        printf("Sal�rio acima da m�dia");
    }
    else{
        printf("Salario de rico");
    }


}
