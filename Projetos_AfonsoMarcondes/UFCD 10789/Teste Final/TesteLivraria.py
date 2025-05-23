def mostrarMenu():
    print("\n************************************************")
    print("*               |Escolhas|                     *")
    print("*                                              *")
    print("*    1 - Cadastrar livro                       *")
    print("*    2 - Procurar por livro                   *")
    print("*    3 - Excluir livro                         *")
    print("*    4 - Ordenar livros                        *")
    print("*    5 - Listar todos os livros cadastrados    *")
    print("*    x - Parar Programa                        *")
    print("*                                              *")
    print("************************************************")

class livros:
    listaLivros = []
    totalLivros = 0
    
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        
        livros.listaLivros.append(self)
        livros.totalLivros += 1
        
    def procurarLivro():
        pesquisar = input("Insira o Titulo/Autor do livro que deseja procurar: ")
        
        for i in livros.listaLivros:
            if i.titulo == pesquisar or i.autor == pesquisar:
                print("\n**Livro Encontrado**")
                print(f"\n| {cont}º Livro |")
                print(f"Titulo: {i.titulo}")
                print(f"Autor: {i.autor}")
                print(f"Ano de Publicação: {i.anoPublicacao}")
                break
            
            print("\n**Livro Não Encontrado**")
                
    def listarLivros():
        cont = 1
        for i in livros.listaLivros:
            print(f"\n| {cont}º Livro |")
            print(f"Titulo: {i.titulo}")
            print(f"Autor: {i.autor}")
            print(f"Ano de Publicação: {i.anoPublicacao}")
            print()
            cont += 1 
while(True):
    mostrarMenu()
        
    escolha = input("Insira a sua escolha: ")

    match escolha:
        case "1":
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            anoPublicacao = input("Ano de Publicação: ")
            
            a = livros(titulo, autor, anoPublicacao)
            
        case "2":
            livros.procurarLivro()
            
        case "5":
            livros.listarLivros()
            
        case "x":
            print("\n\n**Programa Encerrado**")
            break
            
        case _:
            print("\n**Entrada Invalida**")
