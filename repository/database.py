import psycopg2
import os
from utils.funcoes_auxiliares import formata_texto
from utils.valida_cpf_folder import valida_cpf
from utils.valida_data import valida_data_nascimento
from utils.valida_endereco import valida_cep
from utils.valida_rg_folder import valida_rg

class BancoDeDados:

    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()


    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert(self,clientes):



    def select(self,id_cliente):
        print("Selecionando cliente no banco de dados: ")
        select_query = "SELECT * FROM CLIENTE where cpf = '%s';"
        self.cursor.execute(select_query,id_cliente['cpf'])
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        return clientes

    @staticmethod
    def retorna_parametros_conexao_banco_de_dados():
        parametros_conexao = {
            "user": os.getenv('user'),
            "password": os.getenv('password'),
            "host": os.getenv('host'),
            "port": os.getenv('port'),
            "database": os.getenv('database')
        }

        return parametros_conexao

    def update(self,cliente,id_cliente):
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
            infos['data_nascimento'],
            endereco['endereco']['CEP'],
            endereco['endereco']['logradouro'],
            endereco['endereco']['complemento'],
            endereco['endereco']['bairro'],
            endereco['endereco']['cidade'],
            endereco['endereco']['estado'],
            infos['num_casa'],
            id_cliente
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()

    def delete(self,id_cliente):
        print("Selecionando cliente a ser deletado no banco de dados: ")
        delete_query = """DELETE FROM public.cliente
	        WHERE cpf = %s;"""
        self.cursor.execute(delete_query, id_cliente)
        self.connection.commit()

if __name__ == '__main__':

    # Realizar integração com a classe cliente.
    conexao = BancoDeDados()
    id_cliente = {"cpf": "914.566.460-95"}
    conexao.select(id_cliente)

