from banco import Bancodados
from livro import Livro
from emprestimo import Emprestimo
from usuario import Usuario

conn = Bancodados()
conn.conectar()
liv = Livro(conn)
user = Usuario(conn)
empresta = Emprestimo(conn, liv, user)

busca1 = int(input("Qual id do usuario? "))
busca2 = int(input("Qual id do livro? "))
empresta.registrarEmprestimo(busca1, busca2)

#empresta.registraDevolucao(1)

