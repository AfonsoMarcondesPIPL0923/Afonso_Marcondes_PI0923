#include <stdio.h>
#include <stdlib.h>

typedef struct
    {
        char nome[50];
        int matricula;
        float nota;
    }Aluno;

int main(){
    int numero;

    printf("Insira o numero de alunos: ");
    scanf("%d", &numero);

    Aluno *alunos = (Aluno *)malloc(numero * sizeof(Aluno));
    
    if (alunos == NULL) {
        printf("Erro ao alocar memória.\n");
        return 1;
    }

    for(int i = 0; i < numero; i++)
    {
        printf("\n Aluno %d: \n", numero + 1);
        printf("Nome: ")
        fgetc
    }


    free(alunos);
    
    return 0;
}