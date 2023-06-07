import random
import enum
from cliente import Cliente
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca
from conta import Conta
from enumtipoconta import TipoConta


class Banco:

    _lista_clientes = []
    _lista_contas = []

    def __init__(self, nome):
        self._nome = nome
        self._num_agencia = random.randrange(1, 5)

    def _gera_lista_cpf(self):
        lista_cpf = [i.get("cpf") for i in self._lista_clientes]
        return lista_cpf

    def _criar_cliente(self, nome, idade, cpf):
        return Cliente(nome, idade, cpf)

    def _gerar_novo_numero_conta(self):
        while True:
            numero = random.randrange(1, 10)
            if numero not in self._lista_contas:
                break

        self._lista_contas.append(numero)
        return numero

    def _busca_cliente(self, cpf):
        for cliente in self._lista_clientes:
            if cliente.get("cpf") == cpf:
                return cliente

        return False

    def criar_conta_corrente(self, nome, idade, cpf):
        if cpf not in self._gera_lista_cpf():
            cliente = self._criar_cliente(nome, idade, cpf)

            novo_num_cc = self._gerar_novo_numero_conta()

            nova_conta_corrente = ContaCorrente(novo_num_cc, self._num_agencia)
            cliente.associar_nova_conta(nova_conta_corrente)

            dict_cliente = {"cpf": cpf, "conta_corrente": novo_num_cc}
            self._lista_clientes.append(dict_cliente)

            return cliente

        print(f'CPF: {cpf}, já possui uma conta corrente nesse banco')

    def criar_conta_poupanca(self, nome, idade, cpf):
        if cpf not in self._gera_lista_cpf():
            cliente = self._criar_cliente(nome, idade, cpf)

            novo_num_conta = self._gerar_novo_numero_conta()

            nova_conta_poupanca = ContaPoupanca(
                novo_num_conta, self._num_agencia)
            cliente.associar_nova_conta(nova_conta_poupanca)

            dict_cliente = {"cpf": cpf, "conta_poupanca": novo_num_conta}
            self._lista_clientes.append(dict_cliente)

            return cliente

        print(f'CPF: {cpf}, já possui uma conta corrente nesse banco')

    def sacar(self, cliente: Cliente, tipo_conta: TipoConta, valor):
        if tipo_conta == TipoConta.CORRENTE:
            return self._sacar_conta_corrente(cliente, valor)

    def _sacar_conta_corrente(self, cliente: Cliente, valor: float):
        if cliente.get_conta_corrente().num_banco != self._num_agencia:
            print(f'{cliente.nome} não é cliente do banco {self._nome}')
            return False

        cliente_banco = self._busca_cliente(cliente.cpf)
        if cliente_banco:
            if cliente_banco.get("conta_corrente") == cliente.get_conta_corrente().num_conta:
                return cliente.get_conta_corrente().sacar(valor)
