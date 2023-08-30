numeros = []
for i in range(5):
    num = float(input("Ingrese un número: "))
    numeros.append(num)

suma = sum(numeros)
media = suma / 5

print("La media de los números es:", media)

numeros = []
for i in range(5):
    num = float(input("Ingrese un número: "))
    numeros.append(num)

suma = sum(numeros)
media = suma / 5

print("La media de los números es:", media)

import math

numero = int(input("Ingrese un número: "))

if numero < 2:
    print("No es primo")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")

import math

n = int(input("Ingrese un número: "))

for i in range(2, n):
    es_primo = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(i)

n = int(input("Ingrese un número: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("El factorial de", n, "es:", factorial)

n = int(input("Ingrese un número: "))

fibonacci = [0, 1]
while len(fibonacci) < n:
    ultimo = fibonacci[-1]
    penultimo = fibonacci[-2]
    siguiente = ultimo + penultimo
    fibonacci.append(siguiente)

print(fibonacci)
