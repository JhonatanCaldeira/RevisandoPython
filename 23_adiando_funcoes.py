# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    return funcao


soma_com_cinco = criar_funcao(soma)
print(soma_com_cinco(5, 5))

multiplica_por_dez = criar_funcao(multiplica)
print(multiplica_por_dez(10, 10))
