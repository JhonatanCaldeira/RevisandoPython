from classes.fabricante import Fabricante
from classes.carro import Carro
from classes.motor import Motor

honda = Fabricante('honda')
city = honda.fabricar_carro('City')
print(city.fabricante, city.modelo, city.motor)
