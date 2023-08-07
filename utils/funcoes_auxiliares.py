import yfinance
def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado

def share_value(ticket):

    try:
        share = yfinance.Ticker(ticket + '.SA')
        print(f"Procurando valor da ação {share}")
        share_information = share.info
        valor_compra_atual = share_information['ask']
        print(f'O valor de compra atual da ação {ticket} é: {valor_compra_atual:.2f}')
        return valor_compra_atual
    except Exception as e:
        print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
        print(f"Detalhes do erro: {e}")

if __name__ == "__main__":
    share_value()