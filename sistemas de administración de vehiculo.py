# Vamos a
class Vehiculo:
    def __init__(self, marca, modelo):
        #Atributus públicos
        self.marca = marca
        self.modelo = modelo
        #Atributo privado
        self.__kilometraje = 0
#metodo para aumentar el kilometraje
    def conducir(self, km):
        self.__kilometraje += km
#metodo para mostrar el kilometraje actual
    def mostrar_kilometraje(self):
        print(f"kilometraje actual de {self.marca} {self.modelo}: {self.__kilometraje} km.")
#metodo polimorfismo que sera sobrescrito por la clase hija
    def describir(self):
        print(f"{self.marca} {self.modelo} es un vehiculo genérico.")
#clase derivada Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
#sobrescribimos el metodo polimorfismo
    def describir(self):
        print(f"{self.marca} {self.modelo} es un auto con {self.puertas} puertas.")
#clase derivada camion que hereda de vehiculo
class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)
        self.capacidad = capacidad
#subescribimos el metodo polimorfismo
    def describir(self):
        print(f"{self.marca} {self.modelo} es un camion con capacidad de {self.capacidad} toneladas.")
#Llamamos a todas las variables para sus respectivos sobrenombres
auto1 = Auto("Toyota","hilux", 4)
camion1 = Camion("hinno", "GD", 25)

auto1.describir() #muestra la descripcion del auto
auto1.conducir(1300) #simulamos que el auto ha recorrido 1300km
auto1.mostrar_kilometraje() #muestra el kilometraje actual

camion1.describir()  #muestra la descripcion del camion
camion1.conducir(3500) #simulamos que el auto ha recorrido 1300km
camion1.mostrar_kilometraje()  #muestra el kilometraje actual



