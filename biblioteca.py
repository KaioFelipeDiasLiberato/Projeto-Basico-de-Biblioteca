import matplotlib.pyplot as plt
from time import sleep

Livros = []
# classe 
class Biblioteca:
    def __init__ (self, Titulo , Autor , Genero , Quantidade ):
        self.Titulo = Titulo
        self.Autor = Autor
        self.Genero = Genero
        self.Quantidade = Quantidade

def Cadastrar_Livros():
    Novo_livro = str(input("digita o nome do Livro: ")).lower()
    Autor_Livro = str(input("digita o nome do autor do Livro: ")).lower()
    Genero_Livro = str(input("digita o genero do Livro: ")).lower()
    Quantidade_Livro = int(input("digita a quantidade do Livro: "))
    Livros.append(Biblioteca(Novo_livro, Autor_Livro, Genero_Livro, Quantidade_Livro))
    print("livro cadastrado com sucesso.")

def Listar_Livro():
    Titulo_livro = []
    Quantidade_Livros = []
    for lista in Livros:
        print(F"nome: {lista.Titulo}\nAutor: {lista.Autor}\nGenero: {lista.Genero}\nQuantidade: {lista.Quantidade}")
        print("")
        Titulo_livro.append(lista.Titulo)
        Quantidade_Livros.append(lista.Quantidade)

    plt.bar(Titulo_livro, Quantidade_Livros)
    plt.show()
print(f"sistema bibliotecario.".center(60))

def Consultar_Livro():
    Nome_livro = str(input("digita o nome do livro: ")).lower()
    for buscar_Livro in Livros:
        if buscar_Livro.Titulo == Nome_livro:
            print("LIVRO ENCONTRADO...".center(60))
            print(f"Livro: {buscar_Livro.Titulo} \nAutor: {buscar_Livro.Autor} \nQuantidade {buscar_Livro.Quantidade}")
            break
        else:
            print("livro nao encontrado.. ")
            break

while True:
    print("-="*40)
    print("MENU".center(60))
    print("1 = Cadastras um novo livro \n2 = listar os livros \n3 = buscar por titulo \n4=sair")
    escolha = int(input("opição: "))
    print('-='*40)
    sleep(3)
    if escolha == 1:
        Cadastrar_Livros()

    elif escolha == 2:
        print("lista de Livros".center(60))
        Listar_Livro()

    elif escolha == 3:
            print("Consulta por titulo.".center(60))
            Consultar_Livro()
    elif escolha == 4:
        print("obrigado por acessar nosso sistema \nVolte sempre.")
    else:
        print("valor invalido....")
            