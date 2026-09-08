class Usuario():
    def __init__(self, conexao, nome, email, telefone):    
        self.conexao = conexao
        self.nome = nome
        self.email = email
        self.telefone = telefone


    def novoUsuario(self):
        try:
            inserindo = "INSERT INTO usuario (nome, email, telefone) VALUES (%s, %s, %s)"
            self.conexao.executar(inserindo, (self.nome, self.email, self.telefone))
        except Exception as e:
            print(f"O erro é {e}")


    @staticmethod
    def listarUsuario(conexao):
        try:
            busca = "SELECT * FROM usuario"
            resultado = conexao.executar(busca)
            return resultado
        
        except Exception as e:
            print(f"O erro é {e}")

    @staticmethod
    def buscaUsuarioPorId(conexao, valor):
        try:
            busca = "SELECT * FROM usuario WHERE id = %s"
            resultado = conexao.executar(busca, (valor, ))
            return resultado
        except Exception as e:
            print(f"O erro é {e}")

    @staticmethod
    def buscarPorNome(conexao, valor):
        try:
            busca = "SELECT * FROM usuario WHERE nome = %s"
            resultado = conexao.executar(busca, (valor, ))
            return resultado
        
        except Exception as e:
            print(f"O erro é {e}")

    @staticmethod
    def removerUsuario(conexao, id):
        try:
            remover = "DELETE FROM usuario WHERE id = %s"
            conexao.executar(remover, (id, ))
        except Exception as e:
            print(f"O erro é {e}")

    @staticmethod
    def atualizarUsuario(conexao, tabela, novo, onde):
        try:
            atualizar = "UPDATE usuario SET %s = %s WHERE id = %s"
            conexao.executar(atualizar, (tabela, novo, onde))
        except Exception as e:
            print(f"O erro é {e}")