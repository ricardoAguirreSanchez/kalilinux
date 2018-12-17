#lista si deja cambiar datos, no e sinmutable
lista = [12,'Asr',True]
print(lista[1])

lista[1] = 'Zxc'
print(lista[1])

lista.append(12345)
print(lista)


#Diccionario
diccionario = {'clave_1' : 'ASWASWASA', 'clave_2': 100}
print(diccionario.get('clave_2'))
