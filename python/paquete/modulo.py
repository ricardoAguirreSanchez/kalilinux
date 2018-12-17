#multiple asignacion
a,b,c = 1,'joa', '12/02/2018'


def suma():
    """Funcion que pide dos numeros e imprime su suma """
    a = int(input("Ingrese primer valor:"))
    b = int(input("Ingrese segundo valor:"))
    print(a+b)


def multiplica():
    """Funcion que multiplica """
    a = int(input("Ingrese primer numero: "))
    b = int(input("Ingrese segundo numero: "))
    print(a*b)

def fibonacci():
    """Funcion que calcula el fibo"""
    numero = int(input("Ingrese el numero para caclular FIBO: "))
    x, y = 0, 1
    while x < numero:
        print("Fibo es: ",x)
        x = y
        y = x+y
    print()
        
    

