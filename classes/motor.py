class Motor:
    def __init__(self, potencia):
        self._potencia = potencia

    @property
    def potencia(self):
        return self._potencia
