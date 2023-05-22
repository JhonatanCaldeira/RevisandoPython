print("Selecione uma opção.")
opcao = ''
lista = []

while (opcao != 's'):
    opcao = input("[i]nserir, [a]pagar, [l]istar, [s]air: ")

    if opcao == 'i':
        lista.append(input("Informe algo a ser inserido: "))
    elif opcao == 'a':
        indice = input("Informe o indice a ser excluido: ")
        try:
            lista.remove(indice)
        except:
            print("Item não encontrado na lista: ")
    elif opcao == 'l':
        for item, nome in enumerate(lista):
            print(item, nome)
