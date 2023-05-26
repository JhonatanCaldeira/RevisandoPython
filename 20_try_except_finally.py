import sys


try:
    2/0
except ZeroDivisionError as e:
    print('Erro: ', e)
finally:
    print(2/2)

