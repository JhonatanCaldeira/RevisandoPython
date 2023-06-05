class MyContextManager:
    def __init__(self, caminho, modo) -> None:
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo')
        self._arquivo = open(self.caminho, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando')
        self._arquivo.close()

        # return True #Se deixar o return true o python entenderá que a exceção foi tratada.
