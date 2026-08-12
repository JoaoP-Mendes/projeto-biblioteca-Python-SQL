from datetime import date

class Emprestimo():
    def __init__(self, conexao, livro, usuario):
        self.conexao = conexao
        self.livro = livro
        self.usuario = usuario

    def buscaEmprestimoId(self, query):
        try:    
            busca = f"SELECT * FROM emprestimo WHERE id = {query}"
            self.conexao.executar(busca)
            return busca
        except Exception as e:
            print(f"O erro é {e}")

    def registrarEmprestimo(self, idusuario, idlivro):
        try:
            buscausuario = self.usuario.buscaUsuarioPorId(idusuario)
            resultadousuario = buscausuario[0][0]

            if resultadousuario >=  1:
                buscalivro = self.livro.buscarPorId(idlivro)
                resultado = buscalivro[0][4]

                if resultado >= 1:
                    hoje = date.today()
                    print(f"Há {resultado} livros disponíveis")
                    novainfo = resultado - 1
                    self.livro.atulizarLivro("quantidade_disponivel", novainfo, idlivro)

                    registro = f"INSERT INTO emprestimo (livro_id, usuario_id, data_emprestimo, status) VALUES ({idlivro}, {idusuario}, '{hoje}', 'emprestado')"
                    self.conexao.executar(registro)

                    id_emprestimo = self.conexao.executar(registro) #Por algum motivo duplica o Script e são enviados duas vezes o SQL gerando duplicidade
                    print(f"Emprestimo realizado! Anone o ID desse emprestimo {id_emprestimo}")
                else:
                    print(f"Não há livros disponíveis")
        except IndexError as e:
            print("Usuário ou livro não encontrado, por favor, confirme o ID antes de prosseguir")
        except Exception as e:
            print(f"O erro foi {e}")

    def registraDevolucao(self, idemprestismo):
        try:
            atualizarstatus = f"UPDATE emprestimo SET status = 'devolvido' WHERE id = {idemprestismo}"
            self.conexao.executar(atualizarstatus)

            localizarid = f"SELECT * from emprestismo WHERE id = {idemprestismo}"
            self.conexao.executar(localizarid)

            resultadolivroid = localizarid[0][1]


            buscalivro = self.livro.buscarPorId(resultadolivroid)
            quantidadelivros = buscalivro[0][4]
            novaquantidade = quantidadelivros + 1

            self.livro.atulizarLivro("quantidade_disponivel", novaquantidade, resultadolivroid)
        except Exception as e:
            print(f"O erro é esse: {e}")

