import json
import os

BASE_PATH = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_PATH, 'arquivo-python.json')

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open(JSON_FILE, 'w', encoding='utf8') as file:
    json.dump(pessoa, file, indent=2)

with open(JSON_FILE, 'r', encoding='utf8') as file:
    pessoa = json.load(file)
    print(pessoa)
