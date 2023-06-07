from conta import Conta


class ContaPoupanca(Conta):

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self._saldo - valor
        if valor_pos_saque > 0:
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self._saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor:.2f})')

        return self._saldo


if __name__ == '__main__':
    cp1 = ContaPoupanca(1, 1)
    cp1.sacar(1)
