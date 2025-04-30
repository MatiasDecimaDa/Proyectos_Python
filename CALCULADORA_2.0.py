print("PRIMERA CALCULADORA BASICA ____ PYTHON")
print("color 2")

historial = []  

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b


while True:
    
    print("*****MENU******")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    print("5.Ver historial")
    print("6.Salir")

    print("Ingrese la operacion que desea:")
    respuesta = int(input())

    if respuesta == 0 or respuesta > 6:
        print("Opcion invalida. Por favor, ingresa otra opcion")
        continue

    if respuesta == 6:
        print("Gracias por usar la calculadora")
        break


    
    if(respuesta==1):
        a = float(input("Ingresa el primer valor:"))
        b = float(input("Ingresa el segundo valor:"))
        resultado = suma(a,b)
        print("el resultado de la suma es:", resultado)
        historial.append(f"La suma de {a} + {b} = {resultado}")

    elif(respuesta==2):
        a = float(input("Ingresa el primer valor:"))
        b = float(input("Ingresa el segundo valor:"))
        resultado = resta(a,b)
        print("el resultado de la resta es:",resultado)
        historial.append(f"La resta de {a} + {b} = {resultado}")

    elif(respuesta==3):
        a = float(input("Ingresa el primer valor:"))
        b = float(input("Ingresa el segundo valor:"))
        resultado = multiplicacion(a,b)
        print("el resultado de la multiplicacion es:", resultado)
        historial.append(f"La multiplicacion de {a} * {b} = {resultado}")
                          
    elif(respuesta==4):
        a = float(input("Ingresa el primer valor:"))
        b = float(input("Ingresa el segundo valor:"))
        if a == 0 or b == 0:
            print("Ingresa un numero diferente a 0")
            break

        resultado = division(a,b)
        print("El resultado de la division es:",resultado)
        historial.append(f"La division de {a} / {b} = {resultado}")

    elif(respuesta==5):
        print("Historial de operaciones")
        for operaciones in historial:
            print(operaciones)

    continuar = input("Desea continuar en la calculadora (y/n)? ")
    if continuar.lower() != 'y':
        print("Gracias por usar la calculadora")
        break
