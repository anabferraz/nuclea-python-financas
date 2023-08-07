import os


def retorna_parametros_conexao_banco_de_dados():
    print('iniciando')
    parametros_conexao = {
        "user": os.getenv('user'),
        "password": os.getenv('password'),
        "host": os.getenv('host'),
        "port": os.getenv('port'),
        "database": os.getenv('database')
    }
    print("dados coletados: ")
    print(parametros_conexao)
    print(":)")

    return parametros_conexao