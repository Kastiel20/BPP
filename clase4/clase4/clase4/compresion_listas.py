#compresión de listas

numeros = [2,3,4,5,6,7,8]

pares = []

for num in numeros:
    if num %2 == 0:
        pares.append(num)

print(pares)

#sintaxis
#[expresion(i) for i in list]

aux=[]
# for num in numeros:
#     aux.append(num)
aux = [num for num in numeros]
print(aux)

#[expresion(i) for i in list if condition]
# for num in numeros:
#     if num %2 == 0:
#         pares.append(num)
aux=[]
aux = [num for num in numeros if num %2 == 0]

#ejemplos

cuadrados = [num**2 for num in range(10) if num > 5]
print(cuadrados)

cuadrados = [num**2 if num > 5 else None for num in range(10)]
print(cuadrados)

aux_y = []
aux_x = []
for x in range(10):
    aux_y = []
    for y in range(10):
        aux_y.append(y)
    
    aux_x.append(aux_y)
    
aux_final = [[y for y in range(10)] for x in range(10)]

print(aux_final)

some_list = [1,4,7,12,19,22, 23, 26]
new_list = ["{} is even".format(i) if(i%2==0) else "{} It is odd".format(i) for i in some_list]
print(new_list)

#lambda
#sintaxis
#lambda parámetros: expresión

def cuadrado(x):
    return x**2

cuad = lambda x : x**2

#función map()
#aplica una función a cada uno de los elmentos de una lista
#map (una_funcion, una_lista)

enteros = [2,3,4,5,6]
cuadrados= []

for e in enteros:
    cuadrados.append(e**2)


cuadrados = list(map(lambda x : x**2, enteros))

def cuadrado(x):
    return x**2

def cubo(x):
    return x**3

funciones = [cuadrado,cubo]
for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores)


#filter
#filtra una lista de elemento atendiendo al resultado de una función cuando devuelve true
#filter(una_funcion, una_lista)

numeros = [2,3,4,5,6,7,8]

pares = []

for num in numeros:
    if num %2 == 0:
        pares.append(num)


aux_pares= list(filter(lambda x:x%2 ==0, valores))

#reduce
#nos permite hacer calculos acumulativos
from functools import reduce
suma=0
for n in numeros:
    suma+=n

suma = reduce(lambda x,y: x+y, numeros)

suma = sum(numeros)