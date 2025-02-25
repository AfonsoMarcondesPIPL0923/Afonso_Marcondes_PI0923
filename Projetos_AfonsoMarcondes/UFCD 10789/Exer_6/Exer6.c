#include <stdio.h>

int main(){
    char nome[50];
    float compra;
    float desconto;

    printf("Insira o seu nome: ");
    scanf("%49s", nome);

    printf("Insira o valor da compra: ");
    scanf("%f", &compra);

    if(compra > 500){
        desconto = 0.8;
    }
    else if (compra > 200){
        desconto = 0.85;
    }
    else{
        desconto = 0.9;
    }
    
    float total = compra * desconto;

    printf("\nNome: %s\nValor da Compra: %.2f\nDesconto: %d%%\nTotal a Pagar: %.2f\n", nome, compra, &desconto, total);

    return 0;
}
