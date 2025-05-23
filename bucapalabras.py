#busca palabra dento de una oracion

oracion = "hola mi casa es verde claro"
busca = "e"
palabras = oracion.split()

encontradas = [palabra if busca in palabra else "no"  for palabra in palabras ]
print(encontradas)


numeros = list(range(-2,5))
suma = 0
for i in numeros:
    if i > 0 :
        suma = suma +i
print(suma)


numeros = list(range(-2, 5))
suma = sum([i for i in numeros if i > 0])
print(suma)


negativos = list(range(-3,3))
reemplazado = [cambia * -1 if cambia < 0 else cambia for cambia in negativos ]
print(reemplazado)


lst = list(range(0,11))
xxxx = [x + 10  if x >= 5 else x for x in lst  ];print(xxxx)
