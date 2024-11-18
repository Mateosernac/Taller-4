alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def valorLetra(letra):
    letra = letra.upper() 
    if letra in alfabeto:
        return alfabeto.index(letra) + 1  
    return 0  
def calcularPuntos(palabra):
    return sum(valorLetra(letra) for letra in palabra)
print("¡Bienvenido al juego de la palabra de 100 puntos!")
while True:
    palabra = input("Introduce una palabra: ").strip()
    puntos = calcularPuntos(palabra)
    print(f"La palabra \"{palabra}\" tiene {puntos} puntos.")
    if puntos == 100:
        print("¡Felicidades! Has encontrado la palabra de 100 puntos.")
        break
    else:
        print("Sigue intentando...\n")
