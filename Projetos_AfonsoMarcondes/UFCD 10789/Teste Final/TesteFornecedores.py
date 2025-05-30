# Imprimir Menu
def menu():
    print("\n**********************************")
    print("*          |Opções|              *")
    print("*                                *")
    print("*    1 - Adicionar Fornecedor    *")
    print("*    2 - Listar Fornecedores     *")
    print("*    3 - Procurar Fornecedor     *")
    print("*    x - Parar Programa          *")
    print("*                                *")
    print("**********************************")
    
class fornecedor:
    # Lista para guardar os Fornecedores
    listaFornecedores = []
    
    # Numero de Fornecedores Existentes
    contFornecedores = 0
    
    def __init__(self, NomeFor, Endereco, Telefone, NIF, ValorFornecido):
        self.NumFor = fornecedor.contFornecedores
        self.NomeFor = NomeFor
        self.Endereco = Endereco
        self.Telefone = Telefone
        self.NIF = NIF
        self.ValorFornecido = ValorFornecido
        self.Desconto = self.ValorFornecido
        self.ValorFinal = self.ValorFornecido
        
        fornecedor.listaFornecedores.append(self)
        fornecedor.contFornecedores += 1
    
    # Função para Listar Todos os Fornecedores
    @classmethod
    def listarFornecedores(cls):
        if fornecedor.contFornecedores == 0:
            print("\n** Não Existem Fornecedores Registrados **")
            return
        
        for i in cls.listaFornecedores:
            print(f"\n|{i.NumFor + 1}º Fornecedor|")
            print(f"Nome: {i.NomeFor}")
            print(f"Endereco: {i.Endereco}")
            print(f"Telefone: {i.Telefone}")
            print(f"NIF: {i.NIF}")
            print(f"ValorFornecido: {i.ValorFornecido}")
            print(f"Desconto: {i.Desconto}")
            print(f"ValorFinal: {i.ValorFinal}")
            print("_________________________")

    @classmethod
    # Função para Procurar um Fornecedor
    def procurarFornecedor(cls):
        if fornecedor.contFornecedores == 0:
            print("\n** Não Existem Fornecedores Registrados **")
            return
        
        try:
            procurar = int(input("Insira o Numero do Fornecedor Desejado: "))
        
        # Evita que o codigo Crashe   
        except ValueError:
                print("\n** O Valor Inserido está Incorreto **")
                return
            
        for i in cls.listaFornecedores:
            if i.NumFor == procurar - 1:
                print(f"\n|{i.NumFor + 1}º Fornecedor|")
                print(f"Nome: {i.NomeFor}")
                print(f"Endereco: {i.Endereco}")
                print(f"Telefone: {i.Telefone}")
                print(f"NIF: {i.NIF}")
                print(f"ValorFornecido: {i.ValorFornecido}")
                print(f"Desconto: {i.Desconto}")
                print(f"ValorFinal: {i.ValorFinal}")
                print("_________________________")
                return
            
            # Caso não seja encontrado
            print("\n** Fornecedor Não Encontrado **")
            
# Mantem o Programa em Execução
while True:
    # Declaração de Variaveis
    NomeFor = " "
    Endereco = " "
    Telefone = 0
    NIF = 0
    ValorFornecido = 0
    
    # Exibir Menu
    menu()
    
    escolha = input("Insira a sua Escolha: ")
    
    match escolha:
        case "1":
            try:
                print("\n|Insira as Informações do Fornecedor|")
                NomeFor = input(f"Nome: ")
                Endereco = input(f"Endereco: ")
                Telefone = int(input(f"Telefone: "))
                NIF = int(input(f"NIF: "))
                ValorFornecido = int(input(f"ValorFornecido: "))
            
            # Evita que o codigo Crashe
            except ValueError:
                print("\n** O Valor Inserido está Incorreto **")
                
            p1 = fornecedor(NomeFor, Endereco, Telefone, NIF, ValorFornecido)
        
        case "2":
            fornecedor.listarFornecedores()
            
        case "3":
            fornecedor.procurarFornecedor()
        
        case "x":
            print("\n**Programa Encerrado**")
            break
