from banco import Bancodados
from livro import Livro
from emprestimo import Emprestimo
from usuario import Usuario

connObj = Bancodados()
connObj.conectar()
livObj = Livro(connObj)
userObj = Usuario(connObj)
empreObj = Emprestimo(connObj,livObj, userObj)

# while True: 
#     caminho = int(input("O que você deseja verificarr? \n1-- Usuários \n2-- Livros \n3-- Emprestismo\n 4-- Sair\nResposta: "))
#     if caminho == 1:
#         subcaminho = int(input("1 - Adicionar usuario \n2 - Listar \n3 - Buscar por nome \n4 - Remover \n0 - voltar \nResposta: "))
#             if subcaminho == 1: 
#                 nome = str(input("Digite o nome do usuário: "))
#                 email = str(input("Digite o email do usuário: "))
#                 telefone = str(input("Digite o telefone do usuário: "))
#                 userObj.novoUsuario(nome, email, telefone)
#                 print("Usuário cadastrado com sucesso! \n")
#             elif subcaminho == 2:

def menu_livros(livObj):
    while True:
        caminho = int(input("1 - Adicionar usuario \n2 - Listar \n3 - Buscar por nome \n4 - Remover \n0 - voltar \nResposta: "))
        if caminho == 1: 
            nome = str(input("Digite o nome do usuário: "))
            email = str(input("Digite o email do usuário: "))
            telefone = str(input("Digite o telefone do usuário: "))
            userObj.novoUsuario(nome, email, telefone)
            print("Usuário cadastrado com sucesso! \n")

        elif caminho == 2:
            pessoas = livObj.listarUsuario()
            for pessoa in pessoas:
                print(f"{pessoa}\n")

        elif caminho == 3:
            busca = str(input("Digite o nome para busca: "))
            pessoas = livObj.buscaPorNome(busca)


#menu_livros(livObj)