def es_palindromo(frase):

    frase = frase.lower()
    frase = ''.join(c for c in frase if c.isalnum())
    
   
    return frase == frase[::-1]

frase = input("Ingresa una frase: ")

if es_palindromo(frase):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")