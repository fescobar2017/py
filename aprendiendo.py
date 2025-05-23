#numeros = [int(n/2) for n in range(0,100,10)]
#print(numeros)

#numeros = [n for n in range(0,21,2) if n * 2 >10]
#print(numeros)

lista = [par for par in range(0,100) if par % 2 == 0 ]; print(lista)
n = 0
mayor = [n >= x for x in range(0, 100)]
print(n)

from random import *

lista = [n for n in range(0,1400)];print(max(lista))

nombre = "Francisco"
print(min(nombre.lower()))

listado = list(range(0,100));print(listado);print((listado[::-1]))