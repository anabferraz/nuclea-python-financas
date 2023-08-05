from utils.funcoes_auxiliares import formata_texto
from utils.valida_cpf import valida_cpf
from utils.valida_data import valida_data_nascimento
from utils.valida_endereco import valida_cep
from utils.valida_rg import valida_rg

clientes = []
def main():
    validator = True
    while (validator):
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea! Selecione uma das opções abaixo:\n1 - Cliente\n2 - Cadastrar ação\n3 - Realizar análise da carteira\n4 - Imprimir relatório da carteira\n5 - Sair")
        opcao = (input("Digite a opção desejada: "))

        if (opcao=='1'):
            print("1 - Cadastrar Cliente\n2 - Consultar Cliente\n3 - Alterar Cliente\n4 - Deletar Cliente\nInforme os dados do cliente: ")
            cliente = {
                "nome": formata_texto(input ("Nome: ")),
                "cpf": valida_cpf(),
                "rg": valida_rg(),
                "data_nasc": valida_data_nascimento(),
                "endereco": valida_cep(),
                "num_casa": input ("número da casa: ")
            }
            clientes.append(cliente)
            print(clientes)
        elif (opcao=='2'):
            opcao = '2'
        elif (opcao=='3'):
            opcao = '3'
        elif(opcao=='4'):
            opcao = '4'
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