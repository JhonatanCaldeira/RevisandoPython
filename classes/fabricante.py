from classes.carro import Carro
from classes.motor import Motor


class Fabricante:

    def __init__(self, fabricante):
        self._fabricante = fabricante

    @property
    def fabricante(self):
        return self._fabricante

    def fabricar_carro(self, modelo):
        motor = self.fabricar_motor('v6')
        return Carro(modelo, self.fabricante, motor)

    def fabricar_motor(self, potencia):
        return Motor(potencia)
