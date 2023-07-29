validator = True
lista = []
while (validator):
    print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea! Selecione uma das opções abaixo:\n1 - Cadastrar clientes\n2 - Cadastrar ação\n3 - Realizar análise da carteira\n4 - Imprimir relatório da carteira\n5 - Sair")
    opcao = (input("Digite a opção desejada: "))

    if (opcao=='1'):
        print("Informe os dados do cliente:")
        nome = input ("Nome: ")
        lista.append(nome)
        cpf = input ("CPF: ")
        lista.append(cpf)
        rg = input ("RG: ")
        lista.append(rg)
        data_nasc = input ("Data de Nascimento: ")
        lista.append(data_nasc)
        cep = input ("CEP: ")
        lista.append(cep)
        num = input ("número da casa: ")
        lista.append(num)
        print(lista)
    elif (opcao=='2'):
        opcao = '2'
    elif (opcao=='3'):
        opcao = '3'
    elif(opcao=='4'):
        opcao = '4'
    elif(opcao=='5'):
        validator = False
        break
    else :
        print("Opção inválida. Tente novamente.")
        
    ret = input('Deseja retornar para o menú principal?').lower()
    if (ret == 'nao'):
        validator = False
        break
    elif(ret == 'sim'):
        opcao = '0'