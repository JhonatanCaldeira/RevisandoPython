
# lista = [numero * 2 for numero in range(10)]
# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} #Mapeamento com alteracao
    for produto in produtos
    if produto['preco'] > 10 #Filtro
]

print(*novos_produtos, sep='\n')

lista = [
    (x ,y)
    for x in range(3)
    for y in range(3) #For dentro de um outro For
]

print(*lista, sep='\n')