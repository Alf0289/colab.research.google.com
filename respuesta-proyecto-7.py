import random

# Solicitar el nombre de la persona usuaria
nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Generar un token par aleatorio entre 1000 y 9998
token_generado = random.randrange(1000, 9999, 2)

# Mostrar el mensaje con el token generado
print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")

#utilizando random.randint ()
import random

nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Generar número aleatorio y asegurar que sea par
token_generado = random.randint(500, 4999) * 2

print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")

