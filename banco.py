import pymysql.connections
from config import DB_CONFIG


class Bancodados():
    def __init__(self):
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = pymysql.connections.Connection(**DB_CONFIG)

        except Exception as e:
            print(f"An error Occured: {e}")

    def desconectar(self):
        try:
            self.conexao.close()

        except Exception as e:
              print(f"An error Occured: {e}")

    def executar(self, query):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)

            if query.strip().upper().startswith("SELECT"):
                resultado = cursor.fetchall()
                return resultado
            else:
                self.conexao.commit()
                return cursor.lastrowid


        except Exception as e:
            print(f"An error Occured: {e}")
        
