import random
def simulador_clima(dias, temperatura_inicial, prob_lluvia_inicial):
    temperatura = temperatura_inicial
    prob_lluvia = prob_lluvia_inicial
    dias_lluvia = 0
    temperaturas = [temperatura]  
    print(f"Simulación de {dias} días.")
    print(f"Temperatura inicial: {temperatura}°C")
    print(f"Probabilidad inicial de lluvia: {prob_lluvia}%\n")

    for dia in range(1, dias + 1):
        if random.random() < 0.1:
            cambio = random.choice([-2, 2]) 
            temperatura += cambio
            print(f"Día {dia}: Cambio de temperatura {cambio}°C")
        if temperatura > 25:
            prob_lluvia = min(prob_lluvia + 20, 100)  
        elif temperatura < 5:
            prob_lluvia = max(prob_lluvia - 20, 0)   
        llueve = random.random() < (prob_lluvia / 100)
        if llueve:
            dias_lluvia += 1
            print(f"Día {dia}: Llueve 🌧️🌧️🌧️ (100%)")
            temperatura -= 1  
        temperaturas.append(temperatura)
        print(f"Día {dia}: Temperatura = {temperatura}°C, Probabilidad de lluvia = {prob_lluvia}%\n")
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    print("---- Resultados ----")
    print(f"Temperatura máxima: {temp_max}°C")
    print(f"Temperatura mínima: {temp_min}°C")
    print(f"Días con lluvia: {dias_lluvia} días de {dias}")
    print("--------------------")
dias_prediccion = int(input("¿Cuántos días quieres simular?: "))
temp_inicial = float(input("Introduce la temperatura inicial (°C): "))
prob_lluvia_inicial = float(input("Introduce la probabilidad inicial de lluvia (%): "))

simulador_clima(dias_prediccion, temp_inicial, prob_lluvia_inicial)
