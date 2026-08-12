from banco import Bancodados
from livro import Livro
from emprestimo import Emprestimo
from usuario import Usuario

conn = Bancodados()
conn.conectar()
liv = Livro(conn)
user = Usuario(conn)
empresta = Emprestimo(conn, liv, user)


while True:
    resposta = int(input("1 - Realizar emprestimo \n2 - Realizar devolução \n 3 - verificar status \n4 - listar \nResposta: "))
    if resposta == 1: 
        busca1 = int(input("Qual id do usuario? "))
        busca2 = int(input("Qual id do livro? "))
        empresta.registrarEmprestimo(busca1, busca2)

    elif resposta == 2:
        iddevolucao = int(input("Qual o id do emprestimo? "))
        empresta.registraDevolucao(id)

    elif resposta == 3:
        idemprestismo = int(input("Qual o id do emprestimo? "))
        resultado = empresta.buscaEmprestimoId(idemprestismo)
        print(resultado)

    elif resposta == 4:
        resultado = empresta.listarEmprestimo()
        for r in resultado:
            print(r)

    elif resposta == 5:
        break

