class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
    
    def calcularMedia(self,):
        
        
        media = (self.nota1 + self.nota2) / 2
        print()
        print(f"Nome do aluno: {self.nome}")
        print(f"Primeira nota: {self.nota1}") 
        print(f"Segunda nota: {self.nota2}") 
        print(f"Média: {media:.2f}")

        if (media >= 6):
            print("Situação: Aprovado!")
            print()
        else:
            print("Situação: Reprovado!")
            print()
bd = []


while True:
    print("---"*6)
    print("Cadastro de alunos e medias")
    print("---"*6)
    print()
    print("1 - Cadastrar alunos")
    print("2 - Exibir Médias")
    print("3 - Sair do sistema")
    op = input("Escolha uma opção: ")

    if(op == "1"):
        nome = input("Digite o nome do aluno: ")
        nota1 = input("Digite a primeira nota do aluno: ")
        nota2 = input("Digite a segunda nota do aluno: ")
        print("Cadastro efetuado com sucesso!")

        novo_aluno = Aluno(nome, nota1, nota2)
        bd.append(novo_aluno)

    elif(op == "2"):
        if not bd:
            print("Nenhum Aluno Cadastrado")
        else:
            for alunos in bd:
                alunos.calcularMedia()

    elif(op == "3"):
        print("Finalizando o sistema...")
        break
    else:
        print()
        print("Digite uma opção correta!")
        print()