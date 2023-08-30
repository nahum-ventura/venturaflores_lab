def invertir_frase(frase):
    palabras = frase.split()  
    palabras_invertidas = palabras[::-1]  
    frase_invertida = ' '.join(palabras_invertidas)  
    return frase_invertida

frase_original = "Aprendiendo Python con Edem"
frase_invertida = invertir_frase(frase_original)
print(frase_invertida)