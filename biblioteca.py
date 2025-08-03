class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def exibirLivros(self):

        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print("~~~"*3)
        print()

biblioteca = []

while True:

    print("Cadastro de Livros -  Bibliotaca")
    print("~~~"*3)
    print("1 - Cadastrar Livros")
    print("2 - Mostrar Livros")
    print("3 - Sair do sistema")

    opcao = input("Escolha uma opção: ")


    if (opcao =="1"):
        titulo = input("Digite o Título do livro: ")
        autor = input("Digite o Autor do livro: ")
        ano = input("Digite o ano de publicação do livro: ")

        novo_livro = Livro(titulo, autor, ano)
        biblioteca.append(novo_livro)
        print("Cadastro Efetuado com sucesso")

    elif(opcao =="2"):
        cont = 0
        if not biblioteca:
            print("Não existem Livros Cadastrados")
        else:
            for l in biblioteca:
                cont += 1
                print(f"Livro{cont}")
                l.exibirLivros()

    elif(opcao =="3"):
        print("saindo do sistema")
        break

    else:
        print("Opção Inválida, tente novamente!")