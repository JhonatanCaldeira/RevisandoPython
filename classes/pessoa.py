import json


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @sobrenome.setter
    def sobrenome(self, valor):
        self._sobrenome = valor

    def get_nome_completo(self):
        return [self.nome, self.sobrenome]

    def salvar_em_json_file(self, arquivo_json):
        with open(arquivo_json, 'w', encoding='utf8') as arquivo:
            json.dump(self.__dict__, arquivo, indent=2)

    @classmethod
    def extrair_de_json_file(cls, arquivo_json):
        with open(arquivo_json, 'r', encoding='utf8') as arquivo:
            return cls(**json.load(arquivo))
