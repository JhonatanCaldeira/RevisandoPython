from classes.Eletronico import Eletronico
from classes.LogFileMixin import LogFileMixin


class Smartphone(Eletronico, LogFileMixin):
    ...

    def ligar(self):
        super().ligar()
        self.log_success(f'{self._nome} Ligado com sucesso')

    def desligar(self):
        super().desligar()
        self.log_success(f'{self._nome} Desligado com sucesso')


if __name__ == '__main__':
    galaxy_note = Smartphone('galaxy note')
    galaxy_note.ligar()
    galaxy_note.desligar()
