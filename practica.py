numeros = list(range(-3,3))
suma = sum([pos for pos in numeros if pos > 0])
print(suma)

num =list(range(2,10))
pares = [par for par in num if par % 2 ==0]
print(pares)

nega = list(range(-3,3))
cambia = [num if num > 0  else 0 for num in nega];print(cambia)

lst = list(range(0,101))
maximo = max(lst);print(maximo)

import numpy as np

matriz = np.array(([1,2,3],
                   [4,5,6],
                   [7,8,9]))
par =[num for fila in matriz for num in fila if num % 2 == 0];print(par)
impar =[num for fila in matriz for num in fila if num % 2 != 0];print(impar)