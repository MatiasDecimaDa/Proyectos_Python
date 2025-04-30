print("PRIMERA CALCULADORA BASICA ____ PYTHON")


def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b


    
print("*****MENU******")
print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")


print("ingrese la operacion que desea:")
respuesta = int(input())

if respuesta == 0:
    print("Opcion invalida. Por favor, ingresa otra opcion")

a = float(input("ingresa el primer valor:"))
b = float(input("ingresa el segundo valor:"))


if(respuesta==1):
    resultado = suma(a,b)
    print("el resultado de la suma es:", resultado)
elif(respuesta==2):
    resultado = resta(a,b)
    print("el resultado de la resta es:",resultado)
elif(respuesta==3):
    resultado = multiplicacion(a,b)
    print("el resultado de la multiplicacion es:", resultado)
elif(respuesta==4):
    resultado = division(a,b)
    print("el resultado de la division es:",resultado)
