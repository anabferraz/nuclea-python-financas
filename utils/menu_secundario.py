from models.cliente import Cliente
from models.ordem import Ordem
from utils.funcoes_auxiliares import formata_texto
from utils.valida_cpf_folder import valida_cpf
from utils.valida_data import valida_data_nascimento
from utils.valida_endereco import valida_cep
from utils.valida_rg_folder import valida_rg


def menu_cliente_secundario(option):
    if (option == '1'):
        print("Inserindo cliente no banco de dados: ")
        print("Informe os dados do cliente: ")
        cliente = {
            "nome": formata_texto(input("Nome: ")),
            "cpf": valida_cpf(),
            "rg": valida_rg(),
            "data_nasc": valida_data_nascimento(),
            "endereco": valida_cep(),
            "num_casa": input("número da casa: ")
        }
        print(cliente)
        conexao = Cliente()
        conexao.insert(cliente)

    elif (option == '2'):
        conexao = Cliente()
        id_cliente = valida_cpf()
        conexao.select(id_cliente)

    elif (option == '3'):
        conexao = Cliente()
        id_cliente = valida_cpf()
        conexao.update(id_cliente)
        print(f"O cliente de CPF {id_cliente} foi alterado")

    elif (option == '4'):
        conexao = Cliente()
        id_cliente = valida_cpf()
        conexao.delete(id_cliente)
        print(f"O cliente de CPF {id_cliente} foi deletado")

    else:
        print("Opção inválida.")

def menu_ordem_secundario(option):
    if (option == '1'):
        conexao = Ordem()
        id_cliente = valida_cpf()
        conexao.select_shares(id_cliente)
    elif (option == '2'):
        conexao = Ordem()
        id_cliente = valida_cpf()
        conexao.select_share(id_cliente)
    else:
        print("Opção inválida.")