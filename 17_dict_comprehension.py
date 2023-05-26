# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in produto.items()
    if key != 'categoria'
}

print(dc)