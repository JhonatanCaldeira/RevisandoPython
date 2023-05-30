from classes.pessoa import Pessoa
import os

BASE_PATH = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_PATH, 'log', 'jhonatan_caldeira.json')


aluno_1 = Pessoa('Jhon', 'Caldeira', 35)

aluno_1.salvar_em_json_file(JSON_FILE)
aluno_2 = Pessoa.extrair_de_json_file(JSON_FILE)

print("Aluno 01:", aluno_1.get_nome_completo())
print("Aluno 02:", aluno_2.get_nome_completo())

aluno_2.salvar_em_json_file(JSON_FILE)
