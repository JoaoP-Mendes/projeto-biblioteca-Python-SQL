class Usuario():
    def __init__(self, conexao):    
        self.conexao = conexao

    def novoUsuario(self, nome, email, telefone):
        try:
            inserindo = f"INSERT INTO usuario (nome, email, telefone) VALUES ('{nome}', '{email}', '{telefone}')"
            self.conexao.executar(inserindo)
        except Exception as e:
            print(f"O erro é {e}")

    def listarUsuario(self):
        try:
            busca = "SELECT * FROM usuario"
            resultado = self.conexao.executar(busca)
            return resultado
        except Exception as e:
            print(f"O erro é {e}")

    def buscarPorNome(self, query):
        try:
            busca = f"SELECT * FROM usuario WHERE nome = '{query}'"
            resultado = self.conexao.executar(busca)
            return resultado
        except Exception as e:
            print(f"O erro é {e}")

    def removerUsuario(self, id):
        try:
            remover = f"DELETE FROM usuario WHERE id = {id}"
            self.conexao.executar(remover)
        except Exception as e:
            print(f"O erro é {e}")

    def atualizarUsuario(self, tabela, novo, onde):
        try:
            atualizar = f"UPDATE usuario SET {tabela} = '{novo}' WHERE id = {onde}"
            self.conexao.executar(atualizar)
        except Exception as e:
            print(f"O erro é {e}")