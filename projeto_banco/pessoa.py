from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, nome, idade, cpf):
        if not self.valida_cpf(cpf):
            raise ValueError('CPF Invalido')

        self._nome = nome
        self._idade = idade
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def cpf(self):
        return self._cpf

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    def valida_cpf(self, cpf):
        cpf_nove_digitos, cpf_dois_digitos = cpf.split('-')
        cpf_nove_digitos = cpf_nove_digitos.replace('.', '')

        contador_regressivo = 10
        cpf_a_validar = cpf_nove_digitos

        soma_cpf = 0
        for digito in cpf_a_validar:
            soma_cpf += int(digito) * contador_regressivo
            contador_regressivo -= 1

        digito_1 = (soma_cpf * 10) % 11
        primeiro_digito = digito_1 if digito_1 <= 9 else '0'

        contador_regressivo = 11
        cpf_a_validar = cpf_nove_digitos + str(primeiro_digito)

        soma_cpf = 0
        for digito in cpf_a_validar:
            soma_cpf += int(digito) * contador_regressivo
            contador_regressivo -= 1

        digito_2 = (soma_cpf * 10) % 11
        segundo_digito = digito_2 if digito_2 <= 9 else '0'

        if str(digito_1) == cpf_dois_digitos[0] and \
                str(digito_2) == cpf_dois_digitos[1]:
            return True
        # print(f'{primeiro_digito}:{cpf_dois_digitos[0]}')
        # print(f'{segundo_digito}:{cpf_dois_digitos[1]}')
        return False


if __name__ == '__main__':
    p1 = Pessoa('Jhonatan', 32, '137.856.407-50')
    # p1.valida_cpf()
