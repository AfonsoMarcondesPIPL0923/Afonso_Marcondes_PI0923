def menu():
    print("\n********************************")
    print("*          |Opções|            *")
    print("*                              *")
    print("*    1 - Insira um Numero      *")
    print("*    2 - Calcular Tabuada      *")
    print("*    x - Parar Programa        *")
    print("*                              *")
    print("********************************")

# Ver se o numero é primo
def numPrimo(num):
    if num == 1:
        return 0
    for y in range(2, num):
        if num % y == 0:
            return 0
    return 1

def lerNumero(num):
    # Declaração de variaveis
    cont = 0
    
    if num > 30000 or num < 1:
        print("\n** Numero Invalido **")
        return
    
    for i in range(num, 0, -1):
        cont += 1
        
        # Declaração de variaveis
        divisores = 0
        numDivisores = []
        somaDivisores = 0
        
        print(f"|Numero {i}|")
        
        # Ver se o Numero é Primo
        primo = numPrimo(i)
        if primo == 1:
            print(f"** Numero Primo **")
        
        # Calcula o Numero de Divisores
        for y in range(1, i):
            if i % y == 0:
                divisores += 1
                numDivisores.append(y)
                
        print(f"** Tem {divisores} Divisores **")
        
        # Ver se é um Numero Perfeito
        for y in range(len(numDivisores)):
            somaDivisores += numDivisores[y]
            
        if i == somaDivisores:
            print(f"** Numero Perfeito **")
        
        print("____________________________________")
        
        # Parar de 10 em 10
        if cont == 10:
            cont = 0
            parar = input("\nInsira [PARA] para parar, qualquer tecla para continuar: ")
            if parar.lower() == "para":
                return

def calculadora():
    
# Mantem o Programa em Execução
while True:
    # Declaração de variaveis
    num = 0
    
    # Menu de Escolha do Utilizador
    menu()
    
    escolha = input("Insira a sua Escolha: ")
    
    match escolha:
        case "1":
            num = int(input("Insira um Numero: "))
            lerNumero(num)
        
        case "2":
            pass
        
        case "x":
            print("\n** Programa Encerrado **")
            break
        
        case _:
            print("\n** Opção Invalida **")
