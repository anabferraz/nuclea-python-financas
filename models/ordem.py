import psycopg2
import os

from utils.funcoes_auxiliares import share_value
from utils.valida_cpf_folder import valida_cpf
from utils.valida_data import valida_data_compra


class Ordem:

    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()
        self.atributos = None
        self.id_cliente = None
        self.id = None
        self.nome = None
        self.ticket = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def add_share(self):
        self.id_cliente = valida_cpf()
        self.ticket = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
        self.nome = input("Digite a qual empresa a ação pertence: ")
        self.valor_compra = share_value(self.ticket)
        self.quantidade_compra = input("Digite quantas ações você comprou: ")
        self.data_compra = valida_data_compra()

        insert_query = """
                                INSERT INTO share (nome, ticket, valor_compra, quantidade_compra, data_compra, cliente_id)
                                VALUES (%s, %s, %s, %s, %s, %s);
                                """
        values = (
            self.nome, self.ticket, self.valor_compra, self.quantidade_compra, self.data_compra, self.id_cliente,
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        print(values)

    def retorna_parametros_conexao_banco_de_dados(self):
        parametros_conexao = {
            "user": os.getenv('user'),
            "password": os.getenv('password'),
            "host": os.getenv('host'),
            "port": os.getenv('port'),
            "database": os.getenv('database')
        }

        return parametros_conexao

    def select_shares(self, id_cliente):
        print("Selecionando ações no banco de dados: ")
        select_query = (f"SELECT * FROM SHARE where cliente_id = '{id_cliente}';")
        self.cursor.execute(select_query)
        shares = self.cursor.fetchall()
        for share in shares:
            print(share)
        return shares

    def select_share(self, id_cliente):
        ticket = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
        print("Selecionando a ação no banco de dados: ")
        select_query = (f"SELECT * FROM SHARE where cliente_id = '{id_cliente}' AND ticket = '{ticket}';")
        self.cursor.execute(select_query)
        share = self.cursor.fetchall()
        print(share)
        return share