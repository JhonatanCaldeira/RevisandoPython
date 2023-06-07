from pessoa import Pessoa
from conta import Conta
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca


class Cliente(Pessoa):

    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)
        self._conta_corrente = ContaCorrente
        self._conta_poupanca = ContaPoupanca

    def associar_nova_conta(self, nova_conta: Conta):
        if isinstance(nova_conta, ContaCorrente):
            self._conta_corrente = nova_conta
            return True

        self._conta_poupanca = nova_conta

    def get_conta_corrente(self):
        return self._conta_corrente

    def get_conta_poupanca(self):
        return self._conta_poupanca
