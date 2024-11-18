def caracteres_infiltrados(cadena1, cadena2):

    if len(cadena1) != len(cadena2):
        raise ValueError("Las cadenas deben tener la misma longitud.")
    
    infiltrados = [] 
    
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:
            infiltrados.append(cadena2[i])
    
    return infiltrados


cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

try:
    resultado = caracteres_infiltrados(cadena1, cadena2)
    print(f"Caracteres infiltrados: {resultado}")
except ValueError as e:
    print(f"Error: {e}")
