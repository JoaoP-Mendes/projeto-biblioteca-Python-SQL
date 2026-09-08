class Livro():
    def __init__(self, conexao, titulo, autor, ano, quantidade_disponivel):
        self.conexao = conexao
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade_disponivel = quantidade_disponivel

    @property
    def quantidade_disponivel(self):
        return self._quantidade_disponivel

    @quantidade_disponivel.setter
    def quantidade_disponivel(self, valor):
        if valor < 0:
            raise ValueError("Quantidade inválida, informe um número válido")

        else:
            self._quantidade_disponivel = valor


    def novoLivro(self):
        try:
            inserindo = "INSERT INTO livros (titulo, autor, ano, quantidade_disponivel) VALUES (%s, %s, %s, %s)"
            self.conexao.executar(inserindo, self.titulo, self.autor, self.ano, self.quantidade_disponivel)
        except Exception as e:
            print(f"O erro é: {e}")

    @staticmethod
    def listarLivros(conexao):
        try:
            busca = "SELECT * FROM livros"
            resultado = conexao.executar(busca)
            return resultado
        except Exception as e:
            print(f"An error Occured: {e}")

    @staticmethod
    def buscarPorId(conexao, valor):
        try: 
            busca = "SELECT * FROM livros WHERE id = %s"
            resultado = conexao.executar(busca, (valor, ))
            return resultado
        except Exception as e:
            print(f"O erro é: {e}")

    @staticmethod
    def buscarPorTituloOuAutor(conexao, valor):
        try: 
            busca = "SELECT * FROM livros WHERE autor = %s or titulo = %s"
            resultado = conexao.executar(busca, (valor, ))
            return resultado
    
        except Exception as e:
            print(f"O erro é: {e}")

    @staticmethod
    def removerLivro(conexao, valor):
        try:
            remover = "DELETE FROM livros WHERE id = %s"
            conexao.executar(remover, (valor, ))
        except Exception as e:
            print(f"O erro é: {e}")

    @staticmethod
    def atulizarLivro(conexao, tabela, novo, onde):
        try:
            atualizar = "UPDATE livros SET %s = %s WHERE id = %s"
            conexao.executar(atualizar, (tabela, novo, onde))
        except Exception as e:
            print(f"O erro é: {e}")
