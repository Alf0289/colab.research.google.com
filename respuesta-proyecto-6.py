6 - import random

def sorteo_seguidor():
    # Pedir el número de participantes
    participantes = int(input("Ingrese el número de participantes del sorteo: "))
    
    # Realizar el sorteo
    ganador = random.randint(1, participantes)
    
    # Mostrar el resultado
    print(f"🎉 ¡El número sorteado es: {ganador}! 🎉")
    
    return ganador

# Ejecutar el sorteo
if __name__ == "__main__":
    sorteo_seguidor()

    #version mejorada
    import random

def sorteo_seguidor():
    try:
        # Pedir y validar el número de participantes
        participantes = int(input("Ingrese el número de participantes del sorteo: "))
        
        if participantes <= 0:
            print("❌ Error: El número de participantes debe ser mayor a 0")
            return None
        
        # Realizar el sorteo
        ganador = random.randint(1, participantes)
        
        # Mostrar el resultado
        print(f"\n" + "="*40)
        print(f"🎉 SORTEO REALIZADO 🎉")
        print(f"Participantes: {participantes}")
        print(f"¡El número ganador es: {ganador}! 🏆")
        print("="*40)
        
        return ganador
        
    except ValueError:
        print("❌ Error: Por favor ingrese un número válido")
        return None

# Ejecutar el sorteo
if __name__ == "__main__":
    sorteo_seguidor()

    #version con multiples posibilidades
    import random

def realizar_sorteo():
    while True:
        try:
            # Pedir el número de participantes
            participantes = int(input("\nIngrese el número de participantes del sorteo (0 para salir): "))
            
            if participantes == 0:
                print("¡Hasta luego! 👋")
                break
            elif participantes < 0:
                print("❌ Error: El número de participantes no puede ser negativo")
                continue
            
            # Realizar el sorteo
            ganador = random.randint(1, participantes)
            
            # Mostrar el resultado
            print(f"\n🎉 ¡SORTEO REALIZADO!")
            print(f"📊 Total de participantes: {participantes}")
            print(f"🏆 Número ganador: {ganador}")
            
            # Preguntar si quiere hacer otro sorteo
            continuar = input("\n¿Desea realizar otro sorteo? (s/n): ").lower()
            if continuar != 's':
                print("¡Gracias por usar el sistema de sorteos! 👋")
                break
                
        except ValueError:
            print("❌ Error: Por favor ingrese un número válido")

# Ejecutar el programa
if __name__ == "__main__":
    print("🎯 SISTEMA DE SORTEO DE SEGUIDORES 🎯")
    realizar_sorteo()

    