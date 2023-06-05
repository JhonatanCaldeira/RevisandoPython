from classes.MyContextManager import MyContextManager
from pathlib import Path

PATH_TXT = Path(__file__).parent / 'log/contextmanager.txt'

with MyContextManager(PATH_TXT, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
