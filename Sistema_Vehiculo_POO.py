from os import system
system("color 2")
class Vehiculo:

    def __init__(self, marca,modelo,año,color):

        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def adicionar(self):
        
        self.marca = input(f"Ingresa la Marca del Vehiculo: ")
        self.modelo =input(f"Ingresa el Modelo del Vehiculo: ")
        self.año = int(input(f"Ingresa el Año del Vehiculo: "))
        self.color = input(f"Ingresa el Color del Vehiculo: ")

    def mostrar(self):
        
        print("Informacion del Vehiculo")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        


class Auto(Vehiculo):
    def __init__(self,marca = None,modelo = None,año = None,color = None,puertas = None):
        super().__init__(marca,modelo,año,color)
        self.puertas = puertas

    def adicionar(self):
        super().adicionar()
        self.puertas = int(input("Ingrese el Numero de Puertas:"))
        self.mostrar()

    def mostrar(self):
        super().mostrar()
        print(f"Numero de Puerta: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, marca = None, modelo = None, año = None, color = None ,tipo = None):
        super().__init__(marca, modelo, año, color)
        self.tipo = tipo

    def adicionar(self):
        super().adicionar()
        self.tipo = input("Ingrese el Tipo de Moto: ")
        self.mostrar()
    
    def mostrar(self):
        super().mostrar()
        print(f"Tipo de Moto: {self.tipo}")


Vehiculos = []

while True:

    system("cls")
    print("*******MENU*******")
    print("1. Regisrar Auto")
    print("2. Registrar Moto")
    print("3. Mostrar todos los Vehiculos")
    print("4. Salir")
    print("Ingresa la Opcion")
    
    opcion = int(input())

    if opcion == 1:
        nuevo_auto = Auto()
        nuevo_auto.adicionar()
        Vehiculos.append(nuevo_auto)
    
    elif opcion == 2:
        nueva_moto = Moto()
        nueva_moto.adicionar()
        Vehiculos.append(nueva_moto)

    elif opcion == 3:
        for i, vehiculo in enumerate(Vehiculos, start=1):
            print(f"Vehiculo {i}")
            vehiculo.mostrar()
            print("------------------")
            system("pause")

    elif opcion == 4:
        print("Hasta Luego")
        break
    else:
        print("Opcion Invalida")

