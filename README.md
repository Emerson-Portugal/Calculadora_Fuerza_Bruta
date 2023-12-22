# Calculadora de Fuerza Bruta

Este script en Python te permite simular un ataque de fuerza bruta para estimar el tiempo necesario para descifrar una contraseña dada. La estimación se basa en la longitud de la contraseña, la diversidad de caracteres y la tasa de intentos por segundo.

## Uso

1. Ejecuta el script en tu entorno de Python.

```bash

python app.py
```

2. Ingresa la contraseña cuando se solicite.

```plaintext
Ingresa tu contraseña:
```

Observa la salida del script, que mostrará la cantidad de combinaciones posibles y el tiempo estimado para un ataque de fuerza bruta con la tasa de intentos configurada.

## Parámetros Configurables

- **long_password:** Longitud de la contraseña.
- **unico_caracter:** Cantidad de caracteres únicos en la contraseña.
- **intentos:** Tasa de intentos por segundo.

Configura el valor de intentos según el escenario que desees simular. Algunos valores sugeridos:

- intentos = 1: Simula un ataque con un solo intento por segundo.
- intentos = 1000: Simula un ataque con mil intentos por segundo.
- intentos = 10000: Simula un ataque con diez mil intentos por segundo.
- intentos = 1000000: Simula un ataque con un millón de intentos por segundo.
- intentos = 1000000000: Simula un ataque con mil millones de intentos por segundo.

