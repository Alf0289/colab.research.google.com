import math

# Precio por metro cuadrado de césped
PRECIO_POR_M2 = 25.00

# Solicitar el radio del jardín al usuario
print("=== CALCULADORA DE PRECIO DE CÉSPED ===")
radio = float(input("Ingrese el radio del jardín circular (en metros): "))

# Calcular el área del jardín circular
area = math.pi * (radio ** 2)

# Calcular el precio total
precio_total = area * PRECIO_POR_M2

# Mostrar los resultados
print("\n--- RESULTADOS ---")
print(f"Radio del jardín: {radio:.2f} metros")
print(f"Área del jardín: {area:.2f} metros cuadrados")
print(f"Precio por m²: R$ {PRECIO_POR_M2:.2f}")
print(f"PRECIO TOTAL: R$ {precio_total:.2f}")

#version mas simple
# Versión simplificada sin importar math
PRECIO_POR_M2 = 25.00

radio = float(input("Ingrese el radio del jardín circular (en metros): "))

area = 3.14159 * radio * radio
precio_total = area * PRECIO_POR_M2

print(f"Precio total: R$ {precio_total:.2f}")