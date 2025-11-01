import random

# Lista de frutas
frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

# Seleccionar 3 frutas aleatorias sin repetición
ensalada_sorpresa = random.sample(frutas, 3)

# Mostrar el resultado
print("¡Ensalada de frutas sorpresa!")
print("Las frutas seleccionadas son:")
for i, fruta in enumerate(ensalada_sorpresa, 1):
    print(f"{i}. {fruta}")

    #version compactada
    import random

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

ensalada_sorpresa = random.sample(frutas, 3)
print("Ensalada sorpresa con:", ", ".join(ensalada_sorpresa))

