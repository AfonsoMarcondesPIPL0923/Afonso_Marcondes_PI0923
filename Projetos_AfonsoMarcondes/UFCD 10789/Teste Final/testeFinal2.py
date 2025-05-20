class cliente:
    listaClientes = []
    numClientes = 0
    
    def __init__(self, NomCli, morada, tel, nif, compra, Divfin):
        cliente.numClientes += 1
        self.Numcli = cliente.numClientes
        self.NomCli = NomCli
        self.morada = morada
        self.tel = tel
        self.nif = nif
        self.compra = compra
        
        # Calcular o Desconto
        if compra > 99 and compra < 201:
            self.Divfin = cliente.compra * 0.95
            
        elif compra > 200 and compra < 500:
            self.Divfin = cliente.compra * 0.90
        
        elif compra >= 500:
            self.Divfin = cliente.compra * 0.85
        
        else:
            self.Divfin = Divfin
        
        # Adiciona à lista
        cliente.listaClientes.append(self)
        
    @classmethod
    def listarClientes(cls):
        cont = 1
        for i in cls.listaClientes:
            print(f"\n\n|{cont}º Cliente|")
            print(f"Nome: {i.NomCli}")
            print(f"Morada: {i.morada}")
            print(f"Telefone: {i.tel}")
            print(f"NIF: {i.nif}")
            print(f"Valor da Compra (Sem Desconto): {i.compra}")
            print(f"Divida Final (Com Desconto): {i.Divfin}")
            print("____________________________________________")
            cont += 1
            
            para = input("[para] para parar, qualquer outra tecla para continuar:")
            if para == "para" or para == "PARA":
                break
    def procurarCliente(cls, num):
        self.num = num
        
        for i in cls.listaClientes:
            if i.Numcli == num:
                print("\n\n|Cliente Encontrado|")
                print("\n____________________________________________")
                print(f"|{cont}º Cliente|")
                print(f"Nome: {i.NomCli}")
                print(f"Morada: {i.morada}")
                print(f"Telefone: {i.tel}")
                print(f"NIF: {i.nif}")
                print(f"Valor da Compra (Sem Desconto): {i.compra}")
                print(f"Divida Final (Com Desconto): {i.Divfin}")
                print("____________________________________________")
                break
        print("\n\n|Cliente Não Encontrado|")
        
while(True):
    print("\n******************************")
    print("*         |Escolhas|         *")
    print("*                            *")
    print("*    1 - Novo Cliente        *")
    print("*    2 - Listar Clientes     *")
    print("*    3 - Procurar Cliente    *")
    print("*    4 - Parar Programa      *")
    print("*                            *")
    print("******************************")

    escolha = int(input("Insira a sua escolha: "))

    match escolha:
        case 1:
            print(f"\nCadastro do {cliente.numClientes + 1}ºN Cliente")
            NomCli = input("Nome: ")
            morada = input("Morada: ")
            tel = int(input("Telefone: "))
            nif = input("NIF: ")
            compra = int(input("Valor da Compra (Sem Desconto): "))
            Divfin = int(input("Divida Final (Com Desconto): "))
            
            p1 = cliente(NomCli, morada, tel, nif, compra, Divfin)
            
        case 2:
            print("____________________________________________")
            cliente.listarClientes()
            print("\n\n")
        
        case 3:
            proc = int(input("Insira o numero no cliente que pretende procurar: "))
            cliente.procurarCliente(proc)
            print("\n\n")
            
        case 4:
            print("\n**Programa Encerrado**")
            break
