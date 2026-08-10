from banco import Bancodados
from livro import Livro


conn = Bancodados()
conn.conectar()
book = Livro(conn)

"""livros = book.buscarPorTituloOuAutor(input("Nome do autor: "))
print(livros)"""

#Select co id

"""conn = Bancodados()
conn.conectar()
book = Livro(conn)

livros = book.buscarPorId(int(input("Qual id? ")))
print(livros)"""


#Exemplo de mandar livro para o bd
while True:
    resposta = int(input("1 - adicionar livro \n2 - remover livro \n3 - listar \n4 - atualizar \nResposta: "))
    if resposta == 1:
        titulo = input("Insira um titulo: ")
        autor = input("Insira um autor: ")
        ano = int(input("Qual foi ano? "))
        qnt = int(input("Qual a quantidade? "))

        book.novoLivro(titulo, autor, ano, qnt)
    elif resposta == 2: 
        book.removerLivro(int(input("Qual id para remover? ")))

    elif resposta == 3:
        livros = book.listarLivros()
        for livro in livros: 
            print(livro)

    elif resposta == 4:
        idatulizar = int(input("Qual id do livro para atualizar? "))
        oqueatulizar = input("O que você quer atualizar? \nTitulo \nAutor \nAno \nQuantidade \n:").lower()
        if oqueatulizar == "quantidade":
            oqueatulizar = "quantidade_disponivel"

        if oqueatulizar == "quantidade_disponivel" or oqueatulizar == "ano":
            novainfo = int(input("Nova informação: "))
            book.atulizarLivro(oqueatulizar, novainfo, idatulizar)

        elif oqueatulizar == "titulo" or oqueatulizar == "autor":
            novainfo = input("Nova informação: ")
            book.atulizarLivro(oqueatulizar, novainfo, idatulizar)
            

    elif resposta == 5:
        print("Encerrando")
        break
