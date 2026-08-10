class Emprestimo():
    def __init__(self, conexao, livro):
        self.conexao = conexao
        self.livro = livro

    def registrarEmprestimo(self, idlivro):
        buscalivro = self.livro.buscarPorId(idlivro)
        resultado = buscalivro[0][4]

        if resultado >= 1:
            return resultado

        else:
            print("idiota")