import math

def calcular_fuerza_bruta(long_password, unico_caracter, intentos):
    combinaciones_posibles = unico_caracter ** long_password

    tiempo_segundos = combinaciones_posibles / intentos

    dias = int(tiempo_segundos // (3600 * 24))
    horas = int((tiempo_segundos % (3600 * 24)) // 3600)
    minutos = int((tiempo_segundos % 3600) // 60)
    segundos = int(tiempo_segundos % 60)
    return dias, horas, minutos, segundos

# Ingresar la password
password = input("Ingresa tu contraseña: ")


long_password = len(password)

unico_caracter = len(set(password))  


intentos = 1
#intentos = 1000 
#intentos = 10000
#intentos = 1000000
#intentos = 1000000000


dias, horas, minutos, segundos = calcular_fuerza_bruta(long_password, unico_caracter, intentos)

print(f"El tiempo estimado es de aproximadamente {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")
