def detalhes(num):
    print()
    for i in range(num, 1, -1):
        
        # Vê se é um numero perfeito
        lista = []
        for y in range(1, i):
            if i % y == 0:
                lista.append(y)
                
        if sum(lista) == i:
            print(i, "é **NUMERO PERFEITO**")
        
        # Vê se o numero é Primo
        for y in range(2, i): 
            if i % y == 0:
                break
        else:
            print(i, "é **Primo**")
        
        # Lista os divisores do numero
        ls = []
        for y in range(1, i):
            if i % y == 0:
                ls.append(y)
        print("Os divisores de", i, "são:", ls)
        print()
        


while True:
    print("\n****************************")
    print("*       **Escolhas**       *")
    print("*   1 - Insira um Numero   *")
    print("*   2 - Calculadora        *")
    print("*   3 - Sair               *")
    print("*                          *")
    print("****************************\n")
    
    escolha = int(input("Insira a sua escolha: "))
    
    match escolha:
        case 1:
            num = int(input("Insira um numero: "))
            detalhes(num)
            
        case 2:
            break
            
        case 3:
            break
            
        
