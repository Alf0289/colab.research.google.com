1 - pip install matplotlib==3.7.1

2 - import numpy as np

3 - import random

# Lista de números
numeros = [15, 23, 42, 8, 56, 91, 3, 67, 12, 34]

# Elegir un número al azar
numero_aleatorio = random.choice(numeros)

print(f"Lista de números: {numeros}")
print(f"Número elegido al azar: {numero_aleatorio}")

4 - import random

# Generar número entero aleatorio entre 0 y 99
numero_aleatorio = random.randint(0, 99)

print(f"Número entero aleatorio menor que 100: {numero_aleatorio}")

#utilizando numpy
import numpy as np

# Generar número entero aleatorio entre 0 y 99
numero_aleatorio = np.random.randint(0, 100)

print(f"Número entero aleatorio menor que 100: {numero_aleatorio}")

5 - # Solicitar dos números enteros al usuario
print("Calculadora de potencias")
base = int(input("Ingresa el primer número (base): "))
exponente = int(input("Ingresa el segundo número (exponente): "))

# Calcular la potencia
resultado = base ** exponente

# Mostrar el resultado
print(f"\n{base} elevado a la {exponente} = {resultado}")

#utilizando pow ()
# Solicitar dos números enteros al usuario
print("Calculadora de potencias")
base = int(input("Ingresa el primer número (base): "))
exponente = int(input("Ingresa el segundo número (exponente): "))

# Calcular la potencia usando pow()
resultado = pow(base, exponente)

# Mostrar el resultado
print(f"\n{base} elevado a la {exponente} = {resultado}")


