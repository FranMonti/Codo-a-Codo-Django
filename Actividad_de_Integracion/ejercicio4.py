def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        palabra = palabra.lower()  
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

def palabra_mas_repetida(diccionario):
    max_palabra = None
    max_frecuencia = 0
    
    for palabra, frecuencia in diccionario.items():
        if frecuencia > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = frecuencia
    
    return (max_palabra, max_frecuencia)

entrada = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(entrada)
palabra_repetida, frecuencia_maxima = palabra_mas_repetida(resultado)

print("Frecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"{palabra}: {cantidad}")

print(f"Palabra más repetida: {palabra_repetida} (Frecuencia: {frecuencia_maxima})")
