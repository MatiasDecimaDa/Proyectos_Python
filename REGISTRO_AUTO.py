from os import system
system("color 2")

class Auto:
    def __init__ (self, propietario = None,  marca= None,modelo = None,placa = None,color = None, precio = None):

        self.propietario = propietario
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.color = color
        self.precio = precio
        self.arrancado = False


# Metodos para la Class Auto


    def adicionar(self):
        self.propietario = input("Ingrese Nombre de Propietario: ")
        self.marca = input("Ingrese la Marca: ")
        self.modelo = input("Ingrese el Modelo ")
        self.placa = input("Ingrese la Placa: ")
        self.color = input ("Ingrese el Color: ")
        self.precio = float(input("Ingrese el Precio: "))
        print ("Auto Registrado")

    def mostrar(self):
        print("Informacion del Vehiculo")
        print(f"Nombre Propietario: {self.propietario}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Color: {self.color}")
        print(f"Precio:{self.precio}")

    def buscarPlaca(buscarPlaca, autoRegistrado):
        for auto in autoRegistrado:
            if auto.placa == buscarPlaca:
                print("Auto encontrado:")
                auto.mostrar()
                return
            print("Auto no encontrado.")

    def mayorValor(autoRegistrado):
        if len(autoRegistrado) == 0:
            print("No Hay Auto Registrado")
            return
        
        autoMayor = autoRegistrado[0]
        for auto in autoRegistrado:
            if auto.precio > autoMayor.precio:
                autoMayor = auto
        print("El Vehiculo de Mayor Valor es: ")
        autoMayor.mostrar()
    
    def buscarPropietario(buscarPropietario, autoRegistrado):
        if len(autoRegistrado) == 0:
            print("No Hay Autos Registrados")
            return
        
        for nombre in autoRegistrado:
            if nombre.propietario == buscarPropietario:
                print("Propietario Encontrado")
                nombre.mostrar()
            else:
                print("El Propietario No se Encuentra Registrado")

nuevo_auto1 = Auto("Matias Decima","Nissan","2015","3025-ALF","Negro",85500)
nuevo_auto2 = Auto("Eduardo Decima","Toyota","2020","5560-ADS","Blanco",80200)
nuevo_auto3 = Auto("Daniel Gutierrez","Suzuki","2024","6025-MLK","Blanco",14350)
nuevo_auto4 = Auto("Mario Suarez","Hyundai","2010","3032-QWE","Gris",35200)
nuevo_auto5 = Auto("Emmanuel Mercado","Mazda","2024","5962-UAS","Rojo",15500)
nuevo_auto6 = Auto("Sebastiar Chavez","Hyundai","2025","6750-ASS","Azul",15000)
nuevo_auto7 = Auto("Matias Caballero","Kia","2018","3021-DIK","Negro",25200)
nuevo_auto8 = Auto("Ivan Fernandez","Tesla","2024","6076-NIG","Blanco",35200)            

autoRegistrado = [nuevo_auto1,nuevo_auto2,nuevo_auto3,nuevo_auto4,nuevo_auto5,nuevo_auto6,nuevo_auto7,nuevo_auto8]



while True:

    system("cls")
    print("*****MENU*****")
    print("1.Adicionar")
    print("2.Mostrar")
    print("3.Buscar Placa")
    print("4.Mayor Valor")
    print("5.Buscar Propietario")
    print("10.Salir") 
    print("Ingresa la opcion")

    opcion = int(input())

    

    if opcion == 1:   
      nuevo_auto = Auto()
      nuevo_auto.adicionar()
      autoRegistrado.append(nuevo_auto)
    
    elif opcion == 2:

        if len(autoRegistrado) == 0:
            print("No hay autos registrados")

        else:
            print("Auto Registrados: ")
            for i, auto in enumerate(autoRegistrado, start=1):
                print("----------------------------")
                print(f"Auto {i}: ")
                auto.mostrar()
                print("----------------------------")
                system("pause")


    elif opcion == 3:
        if len(autoRegistrado) == 0:
            print("No Hay Auto registrado para buscar")
        else:
            buscarPlaca = input("Ingrese el Numero de Placa del Vehiculo: ")
            Auto.buscarPlaca(buscarPlaca, autoRegistrado)
            system("pause")


    elif opcion == 4:
        Auto.mayorValor(autoRegistrado)
        system("pause")


    elif opcion == 5:
        buscarPropietario = input("Ingresa el nombre del Propietario:")
        Auto.buscarPropietario(buscarPropietario, autoRegistrado)
        system("pause")


    elif opcion == 10:
        print("Hasta Luego!!!")
        break
    else:
        print("Opcion Invalida")
        