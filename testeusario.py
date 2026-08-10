from banco import Bancodados
from usuario import Usuario

conn = Bancodados()
conn.conectar()
users = Usuario(conn)

while True: 
    resposta = int(input("1 - Adicionar usuario \n2 - Listar \n3 - Buscar por nome \n4 - Remover \n0 - Sair \nResposta: "))
    if resposta == 1:
        nome = input("Qual o nome? ")
        email = input("Qual o email? ")
        telefone = input("Qual telefone? ")

        users.novoUsuario(nome, email, telefone)
    elif resposta == 2:
        user = users.listarUsuario()
        for pessoa in user:
            print(pessoa)

    elif resposta == 3:
        buscanome = input("Qual o nome do usuario? ")
        user = users.buscarPorNome(buscanome)
        for nome in user:
            print(nome)

    elif resposta == 4:
        id = int(input("Qual o id do usuário para remoção? "))
        users.removerUsuario(id)

    elif resposta == 5:
        idatulizar = int(input("Qual id do usuario para atualizar? "))
        oqueatulizar = input("O que você quer atulizar? \nNome \nEmail \nTelefone \n: ").lower()
        novainfo = input("Nova informação: ")
        users.atualizarUsuario(oqueatulizar, novainfo, idatulizar)
    
            
    elif resposta == 0:
        break