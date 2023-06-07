from abc import ABC, abstractmethod


@abstractmethod
class Conta(ABC):

    def __init__(self, num_conta: int, num_banco: int, saldo_inicial: int | float = 0.0) -> None:
        self._num_conta = num_conta
        self._num_banco = num_banco
        self._saldo = saldo_inicial

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    @property
    def num_conta(self):
        return self._num_conta

    @property
    def num_banco(self):
        return self._num_banco

    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> float:
        self._saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
        return self._saldo

    def detalhes(self, msg='') -> None:
        print(f'O seu saldo é {self._saldo:.2f} {msg}')
