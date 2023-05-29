# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os
import json

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'tarefas.json')


def debug(func):
    def _debug(*args, **kwargs):
        retorno = func(*args, **kwargs)
        print(f'{func.__name__}(args: {args}, kwargs: {kwargs}) -> {retorno}')
        return retorno
    return _debug


def listar_atividades(lista=None):
    print()
    for item in lista:
        print(item)


def add_atividade(tarefa, tarefas):
    if not tarefa.strip():
        print()
        print('Informe uma tarefa para ser adicionada')
        return

    tarefas.append(tarefa)


def desfazer_atividade(lista, lista_tarefas_excluidas):
    if lista == None or not lista:
        print()
        print('Nada a desfazer')
        return
    else:
        lista_tarefas_excluidas.append(lista.pop())


def refazer_atividade(lista_tarefas, lista_tarefas_excluidas):
    if not lista_tarefas_excluidas:
        print('Nada a refazer')
        print()
    else:
        lista_tarefas.append(lista_tarefas_excluidas.pop())


def ler(tarefas, caminho_arquivo):
    dados = []
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)


lista_tarefas = ler([], JSON_FILE)
lista_tarefas_excluidas = []
while True:
    print()
    print("Comandos: listar, desfazer, refazer.")
    tarefa_comando = input("Digite uma tarefa ou um comando:")

    if (tarefa_comando not in ['listar', 'desfazer', 'refazer', 'clear']):
        add_atividade(tarefa_comando, lista_tarefas)
        listar_atividades(lista_tarefas)
    else:
        if tarefa_comando == 'listar':
            listar_atividades(lista_tarefas)
        elif tarefa_comando == 'desfazer':
            desfazer_atividade(lista_tarefas, lista_tarefas_excluidas)
            listar_atividades(lista_tarefas)
        elif tarefa_comando == 'refazer':
            refazer_atividade(lista_tarefas, lista_tarefas_excluidas)
            listar_atividades(lista_tarefas)
        else:
            os.system('cls')

    salvar(lista_tarefas, JSON_FILE)
