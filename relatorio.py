import yfinance

def obter_dados_acao(ticker, nome_arquivo):
    try:
        # Obter os dados da ação usando o Yahoo Finance (B3)
        acao = yfinance.download(ticker + '.SA', progress=False)

        # Exibir os dados
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatorio da acao: " + ticker + "\n")
            arquivo.write(str(acao.tail()))

        print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

    except Exception as e:
        print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
        print(f"Detalhes do erro: {e}")

if __name__ == "__main__":
    # Obter e mostrar os dados da ação e exportar para o arquivo
    obter_dados_acao()