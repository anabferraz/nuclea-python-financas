import yfinance
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from models.ordem import Ordem
from utils.valida_cpf_folder import valida_cpf


def analisar_carteira():
    # Definir o período de data desejado
    start_date = "2020-01-01"
    end_date = datetime.now().date()

    conexao = Ordem()
    lista = []
    cpf = valida_cpf()
    conexao.analise_carteira_select(cpf)


    # Criar um DataFrame vazio
    df = pandas.DataFrame()

    # Baixar os dados para cada ação e adicionar ao DataFrame
    for i in lista:
        cotacao = yfinance.download(i, start=start_date, end=end_date)
        df[i] = cotacao['Adj Close']

    # Plotar as séries de preços do DataFrame
    df.plot(figsize=(15, 10))

    plt.xlabel('Anos')
    plt.ylabel('Valor Ticket')
    plt.title('Variação de valor das ações')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    analisar_carteira()