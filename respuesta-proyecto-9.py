import math

# Lista de números proporcionada
numeros = [2, 8, 15, 23, 91, 112, 256]

print("Análisis de raíces cuadradas:")
print("-" * 40)

# Lista para almacenar los números que tienen raíz cuadrada entera
raices_enteras = []

for numero in numeros:
    raiz = math.sqrt(numero)
    es_entero = raiz.is_integer()
    
    print(f"√{numero} = {raiz:.4f} {'✓ ENTERO' if es_entero else ''}")
    
    if es_entero:
        raices_enteras.append(numero)

print("-" * 40)
print(f"Números con raíz cuadrada entera: {raices_enteras}")
print(f"Cantidad total: {len(raices_enteras)}")

# Mostrar las raíces exactas
if raices_enteras:
    print("\nRaíces exactas:")
    for num in raices_enteras:
        print(f"√{num} = {int(math.sqrt(num))}")

#version compactada

import math

numeros = [2, 8, 15, 23, 91, 112, 256]

# Encontrar números con raíz cuadrada entera usando comprensión de listas
raices_enteras = [num for num in numeros if math.sqrt(num).is_integer()]

print(f"Números originales: {numeros}")
print(f"Números con raíz cuadrada entera: {raices_enteras}")
