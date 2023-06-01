from classes.motor import Motor


class Carro:
    def __init__(self, modelo, fabricante, motor):
        self._modelo = modelo
        self._fabricante = fabricante
        self._motor = motor

    @property
    def modelo(self):
        return self._modelo

    @property
    def fabricante(self):
        return self._fabricante

    @property
    def motor(self):
        return self._motor.potencia

    @motor.setter
    def motor(self, motor):
        self._motor = motor
