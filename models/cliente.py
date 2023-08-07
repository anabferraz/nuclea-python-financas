import psycopg2
import os

from utils.funcoes_auxiliares import formata_texto
from utils.valida_data import valida_data_nascimento
from utils.valida_endereco import valida_cep
from utils.valida_rg_folder import valida_rg


class Cliente:

    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()
        self.cpf = None
        self.id = None
        self.nome = None
        self.rg = None
        self.data_nascimento = None
        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.cidade = None
        self.estado = None
        self.num_casa = None

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, cliente):
        self.cpf = cliente['cpf']
        self.nome = cliente['nome']
        self.rg = cliente['rg']
        self.data_nascimento = cliente['data_nasc']
        self.cep = cliente['endereco']['CEP']
        self.logradouro = cliente['endereco']['Logradouro']
        self.complemento = cliente['endereco']['Complemento']
        self.bairro = cliente['endereco']['Bairro']
        self.cidade = cliente['endereco']['Cidade']
        self.estado = cliente['endereco']['Estado']
        self.num_casa = cliente['num_casa']

        insert_query = """
                        INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro, complemento,
        	            bairro, cidade, estado, numero_residencia)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """
        values = (
            self.nome, self.cpf, self.rg, self.data_nascimento, self.cep, self.logradouro, self.complemento,
            self.bairro, self.cidade, self.estado, self.num_casa
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        return cliente

    def select(self, id_cliente):
        print("Selecionando cliente no banco de dados: ")
        select_query = (f"SELECT * FROM CLIENTE where cpf = '{id_cliente}';")
        self.cursor.execute(select_query)
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        return clientes

    def update(self, id_cliente):
        print("Selecionando cliente a ser alterado no banco de dados: ")
        update_query = ("""UPDATE public.cliente 
                SET nome = %s, rg = %s, data_nascimento = %s, cep = %s, logradouro = %s, complemento = %s,
        	            bairro = %s, cidade = %s, estado = %s, numero_residencia = %s
                WHERE cpf = %s;""")

        endereco = {
            "endereco": valida_cep()
        }
        infos = {
            "nome": formata_texto(input("Nome: ")),
            "rg": valida_rg(),
            "data_nasc": valida_data_nascimento(),
            "num_casa": input("número da casa: ")
        }

        values = (
            infos['nome'],
            infos['rg'],
            infos['data_nasc'],
            endereco['endereco']['CEP'],
            endereco['endereco']['Logradouro'],
            endereco['endereco']['Complemento'],
            endereco['endereco']['Bairro'],
            endereco['endereco']['Cidade'],
            endereco['endereco']['Estado'],
            infos['num_casa'],
            id_cliente
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()

    def delete(self, id_cliente):
        print("Selecionando cliente a ser deletado no banco de dados: ")
        delete_query = (f"""DELETE FROM public.cliente
        	        WHERE cpf = '{id_cliente}';""")
        self.cursor.execute(delete_query)
        self.connection.commit()

    def retorna_parametros_conexao_banco_de_dados(self):
        parametros_conexao = {
            "user": os.getenv('user'),
            "password": os.getenv('password'),
            "host": os.getenv('host'),
            "port": os.getenv('port'),
            "database": os.getenv('database')
        }

        return parametros_conexao
