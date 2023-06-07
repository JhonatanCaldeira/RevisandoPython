from conta import Conta


class ContaCorrente(Conta):

    def __init__(self, num_conta: int, num_banco: int, saldo_inicial: float = 0) -> None:
        super().__init__(num_conta, num_banco, saldo_inicial)
        self._limite_especial = 100.0

    @property
    def limite_especial(self):
        return self._limite_especial

    @limite_especial.setter
    def limite_especial(self, valor: float):
        self._limite_especial = valor

    def sacar(self, valor: float) -> float:
        if valor > (self._saldo + self._limite_especial):
            print('Saldo insuficiente')
            print(f'Saldo atual: {self._saldo}')
            print(f'Seu limite: {self._limite_especial}')
            return self._saldo

        self._saldo -= valor
        if self._saldo < 0:
            self._limite_especial -= abs(self._saldo)
            self._saldo = 0.0

        return valor
