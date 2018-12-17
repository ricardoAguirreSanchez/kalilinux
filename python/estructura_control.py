numero = 0

#estructura de control condicional
if numero > 0:
    print('es mayor a cero')
elif numero < 0:
    print('es menor a cero')
else:
    print('es cero')

#estructura de contro iterativa
print('Ingrese un numero entero')
numero = int(input("Digite un numero:"))
contador = 0
while contador < numero:
    contador = contador + 1
    print(contador)

#estructura de control iterativa FOR
lista = ['java','reactjs','sql']
for lenguaje in lista:
    print(lenguaje)

for edad in range(10,17):
    print("Tu edad es: ", edad)


