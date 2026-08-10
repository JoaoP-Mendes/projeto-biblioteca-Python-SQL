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


        except Exception as e:
            print(f"An error Occured: {e}")
        



"""class Vendedos():
    def __init__(self, nome): 
        self.nome = nome
        self.vendas = 0 

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(f"{self.nome} bateu a meta") 
        else:
            print(f"{self.nome} não bateu a meta") 

vendedor1 =  Vendedos("Mendes")
vendedor1.vendeu(100)
vendedor1.bateu_meta(500)"""
