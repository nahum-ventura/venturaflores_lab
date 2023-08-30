Alfabeto='  ABCDEFGHIJKLMNÑOPQRSTVWXYZ'

mensaje=""
Clave= 7
cifrado=" "
for letra in mensaje.upper():
    if letra in Alfabeto:
        indice= Alfabeto.find(letra)
        indice +=Clave
        if indice>=27:
            indice-=27
        cifrado+=Alfabeto[indice]
    else:
        cifrado+=letra

print(cifrado)