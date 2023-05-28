from itertools import permutations, combinations, product


def print_interavel(interavel):
    print(*interavel, sep='\n')


pessoas = ['Jhon', 'Helio', 'Brii', 'Maria']

camisas = [
    ['branca', 'preta'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex']
]

# print_interavel(permutations(pessoas))
# print_interavel(combinations(pessoas, 2))

print_interavel(product(*camisas))
