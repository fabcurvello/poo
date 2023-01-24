class OpcaoInvalidaError(Exception):
    pass


def selecione_opcao(opcao):
    if (opcao == "1"):
        print("1 - Cartões de Crédito")
    elif (opcao == "2"):
        print("2 - Cartões de Débito")
    elif (opcao == "3"):
        print("3 - PIX")
    else:
        raise OpcaoInvalidaError("Opção inválida")


try:
    opcao = input("Informe o número da opção desejada: ")
    selecione_opcao(opcao)
except OpcaoInvalidaError as erro:
    print(erro)