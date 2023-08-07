from analise_carteira import analisar_carteira
from models.cliente import Cliente
from models.ordem import Ordem
from utils.menu_secundario import menu_cliente_secundario


clientes = []
def main():

    cliente = Cliente()
    validator = True
    while (validator):
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea! Selecione uma das opções abaixo:\n1 - Cliente\n2 - Cadastrar ação\n3 - Realizar análise da carteira\n4 - Imprimir relatório da carteira\n5 - Sair")
        opcao = (input("Digite a opção desejada: "))

        if (opcao=='1'):
            option = input("Selecione a opção desejada:\n1 - Cadastrar Cliente\n2 - Consultar Cliente\n3 - Alterar Cliente\n4 - Deletar Cliente\n")
            menu_cliente_secundario(option)

        elif (opcao=='2'):
            ordem = Ordem()
            ordem.add_share()
        elif (opcao=='3'):
            analisar_carteira()
        elif(opcao=='4'):
            pass
        elif(opcao=='5'):
            print("Obrigada por utilizar o sistema de gerenciamento de carteira de ações da Nuclea! Até a próxima! :)")
            validator = False
            break
        else :
            print("Opção inválida. Tente novamente.")

        ret = input('Deseja retornar para o menú principal?').lower()
        if (ret == 'nao'):
            print("Obrigada por utilizar o sistema de gerenciamento de carteira de ações da Nuclea! Até a próxima! :)")
            validator = False
            break
        elif(ret == 'sim'):
            opcao = '0'

if __name__ == "__main__":
    main()