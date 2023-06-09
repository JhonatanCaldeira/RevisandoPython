from functools import partial


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)


def mudar_preco_de_produto(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = list(map(mudar_preco_de_produto, produtos))

novos_produtos_2 = [
    {**produto, 'preco': round((produto['preco'] * 1.1), 2)}
    for produto in produtos
]

# novos_produtos_2 = list(map(lambda a: round((a['preco']*1.1), 2), produtos))

print_iter(novos_produtos)
print_iter(novos_produtos_2)
