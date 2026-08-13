from banco import Bancodados
from livro import Livro
from emprestimo import Emprestimo
from usuario import Usuario

connObj = Bancodados()
connObj.conectar()
livObj = Livro(connObj)
userObj = Usuario(connObj)
empreObj = Emprestimo(connObj,livObj, userObj)

def menu_usuario(userObj):
    while True:
        try:
            caminho = int(input("1 - Adicionar usuario \n2 - Listar \n3 - Buscar por nome \n4 - Remover \n5 - Atualizar usuário \n0 - Voltar menu \nResposta: "))
            if caminho == 1: 
                nome = str(input("Digite o nome do usuário: "))
                email = str(input("Digite o email do usuário: "))
                telefone = str(input("Digite o telefone do usuário: "))
                userObj.novoUsuario(nome, email, telefone)
                print("Usuário cadastrado com sucesso! \n")

            elif caminho == 2:
                pessoas = userObj.listarUsuario()
                for pessoa in pessoas:
                    print(f"{pessoa}\n")

            elif caminho == 3:
                busca = str(input("Digite o nome para busca: "))
                pessoas = userObj.buscarPorNome(busca)
                print(f"{pessoas}\n")

            elif caminho == 4:
                buscaremocao = int(input("Digite o ID do usuário para remoção: "))
                userObj.removerUsuario(buscaremocao)
                print("Usuário removido com sucesso! \n")

            elif caminho == 5:
                idatulizar = int(input("Digite o ID do usuário para  atualizar: "))
                oqueatulizar = input("O que você quer atualizar \nNome \nEmail \nTelefone \nResposta: ").lower()
                novainfo = input("Digite a nova atulização: ")
                userObj.atualizarUsuario(oqueatulizar, novainfo, idatulizar)
                print("Atualização realizada com sucesso!\n")

            elif caminho == 0:
                print("Voltando para o menu... \n")
                break

            else:
                print("Comando não encontrado! Selecione uma opção valida \n")
        except Exception as e:
            print(f"Erro inesperado: {e} \n")
            continue

def menu_livro(livObj):
    while True:
        try:
            caminho = int(input("1 - Adicionar novo livro \n2 - Remover livro \n3 - listar \n4 - Atualizar livro \n0 - Voltar menu \nResposta: "))
            if caminho == 1:
                titulo = str(input("Digite o título do livro: "))
                autor = str(input("Digite o autor do livro: "))
                ano = int(input("Digite o ano de publicação: "))
                qnt = int(input("Digite a quantidade de livros para estoque: "))

                livObj.novoLivro(titulo, autor, ano, qnt)
                print("Livro adicionado no estoque!\n")

            elif caminho == 2:
                idremocao = int(input("Digite o do livro para remoção: "))
                livObj.removerLivro(idremocao)
                print("Livro removido do estoque com sucesso!\n")

            elif caminho == 3:
                livros = livObj.listarLivros()
                for livro in livros:
                    print(f"{livro}\n")

            elif caminho == 4:
                idatulizar = int(input("Digite ID do livro para atualização: "))
                oqueatulizar = input("O que você quer atualizar? \nTitulo \nAutor \nAno \nQuantidade \nResposta:").lower()
                if oqueatulizar == "quantidade":
                    oqueatulizar = "quantidade_disponivel"
        
                if oqueatulizar == "quantidade_disponivel" or oqueatulizar == "ano":
                    novainfo = int(input("Nova informação: "))
                    livObj.atulizarLivro(oqueatulizar, novainfo, idatulizar)
                    print("Atualizado com sucesso!\n")
        
                elif oqueatulizar == "titulo" or oqueatulizar == "autor":
                    novainfo = input("Nova informação: ")
                    livObj.atulizarLivro(oqueatulizar, novainfo, idatulizar)
                    print("Atualizado com sucesso!\n")

            elif caminho == 0:
                print("Voltando para o menu... \n")
                break

            else:
                print("Comando não encontrado! Selecione uma opção valida \n")
        except Exception as e:
            print(f"Erro inesperado: {e} \n")
            continue

def menu_emprestimo(empreObj):
    while True:
        try:
            caminho = int(input("1 - Realizar emprestimo \n2 - Realizar devolução \n3 - Verificar status \n4 - Listar \n0 - Voltar menu \nResposta: "))
            if caminho == 1:
                idusuario = int(input("Digite o ID do usuário para o emprestimo: "))
                idlivro = int(input("Digite o ID do livro para o emprestimo: "))
                empreObj.registrarEmprestimo(idusuario, idlivro)

            elif caminho == 2:
                idemprestismo = int(input("Digite o ID do emprestimo: "))
                empreObj.registraDevolucao(idemprestismo)
                print("Devolução realizada com sucesso!\n")

            elif caminho == 3:
                idemprestismo = int(input("Digite o ID do emprestimo: "))
                busca = empreObj.buscaEmprestimoId(idemprestismo)
                print(f"{busca}\n")

            elif caminho == 4:
                buscas = empreObj.listarEmprestimo()
                for busca in buscas:
                    print(f"{busca}\n")

            elif caminho == 0:
                print("Voltando para o menu... \n")
                break

            
            else:
                print("Comando não encontrado! Selecione uma opção valida\n")

        except Exception as e:
            print(f"Erro inesperado: {e} \n")
            continue

while True:
    try: 
        escolhamenhu = int(input("Qual menu deseja verificar? \n1 -- MENU USUÁRIOS \n2 -- MENU LIVROS \n3 -- MENU EMPRESTISMOS \n0 -- ENCERRAR \nRESPOSTA: "))        
        if escolhamenhu == 1:
            menu_usuario(userObj)

        elif escolhamenhu == 2:
            menu_livro(livObj)

        elif escolhamenhu == 3:
            menu_emprestimo(empreObj)  

        elif escolhamenhu == 0:
            print("Encerrando programa...")
            break
        else:
            print("Escolha um menu valido\n")
    except Exception as e:
        print(f"Ocorru um erro inesperado: {e} \n")
        continue