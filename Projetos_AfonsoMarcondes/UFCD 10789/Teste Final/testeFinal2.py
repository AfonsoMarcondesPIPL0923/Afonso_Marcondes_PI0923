class cliente:
    listaClientes = []
    numClientes = 0
    
    def __init__(self, Numcli, NomCli, morada, tel, nif, compra, Divfin):
        cliente.numClientes += 1
        self.Numcli = numClientes
        self.NomCli = NomCli
        self.morada = morada
        self.tel = tel
        self.nif = nif
        self.compra = compra
        self.Divfin = Divfin
        cliente.listaClientes.append(self)
        
    @classmethod
    def listarClientes(cls):
        for i in cls.listaClientes:
            print(f"**{i+1}º Cliente**")
            print(f"Nome: {i.NomCli}")
            print(f"Morada: {i.morada}")
            print(f"Telefone: {i.tel}")
            print(f"NIF: {i.nif}")
            print(f"Valor da Compra (Sem Desconto): {i.compra}")
            print(f"Divida Final (Com Desconto): {i.Divfin}")


while(True):
    print("******************************")
    print("*         |Escolhas|         *")
    print("*                            *")
    print("*    1 - Novo Cliente        *")
    print("*    2 - Listar Clientes     *")
    print("*    3 - Parar Programa      *")
    print("*                            *")
    print("******************************")

    escolha = int(input("Insira a sua escolha: "))

    match escolha:
        case 1:
            print(f"Cadastro do {numClientes + 1}ºN Cliente")
            NomCli = input("Nome: ")
            morada = input("Morada: ")
            tel = int(input("Telefone: "))
            nif = input("NIF: ")
            compra = int(input("Valor da Compra (Sem Desconto): "))
            Divfin = int(input("Divida Final (Com Desconto): "))
            
            p1 = cliente(NomCli, morada, tel, nif, compra, Divfin)
            
        case 2:
            print("2")
        case 3:
            print("\n**Programa Encerrado**")
            break
