from banco import Bancodados
from livro import Livro
from emprestimo import Emprestimo

conn = Bancodados()
conn.conectar()
liv = Livro(conn)
empresta = Emprestimo(conn, liv)

resultado = empresta.registrarEmprestimo(int(input("Qual id do livro? ")))
print(f"Quantidade disponível: {resultado}")


