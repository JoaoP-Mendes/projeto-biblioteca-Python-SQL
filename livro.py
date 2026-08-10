class Livro():
    def __init__(self, conexao):
        self.conexao = conexao

    def novoLivro(self, titulo, autor, ano, quantidade_disponivel):
        try:
            inserindo = f"INSERT INTO livros (titulo, autor, ano, quantidade_disponivel) VALUES ('{titulo}', '{autor}', {ano}, {quantidade_disponivel})"
            self.conexao.executar(inserindo)
        except Exception as e:
            print(f"An error Occured: {e}")

    def listarLivros(self):
        try:
            busca = "SELECT * FROM livros"
            resultado = self.conexao.executar(busca)
            return resultado
        except Exception as e:
            print(f"An error Occured: {e}")

    def buscarPorId(self, query):
        try: 
            busca = f"SELECT * FROM livros WHERE id = {query}"
            resultado = self.conexao.executar(busca)
            return resultado
        except Exception as e:
            print(f"An error Occured: {e}")

    def buscarPorTituloOuAutor(self, query):
        try: 
            busca = f"SELECT * FROM livros WHERE autor = '{query}' or titulo = '{query}'"
            resultado = self.conexao.executar(busca)
            return resultado
    
        except Exception as e:
            print(f"An error Occured: {e}")


    def removerLivro(self, id):
        try:
            remover = f"DELETE FROM livros WHERE id = {id}"
            self.conexao.executar(remover)
        except Exception as e:
            print(f"An error Occured: {e}")

    def atulizarLivro(self, tabela, novo, onde):
        try:
            atualizar = f"UPDATE livros SET {tabela} = '{novo}' WHERE id = {onde}"
            self.conexao.executar(atualizar)
        except Exception as e:
            print(f"An error Occured: {e}")