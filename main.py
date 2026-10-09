import random

# ==========================================
# PERSONA 1: Menú Principal
# ==========================================
def mostrar_menu():
    print("---------------------------------")
    print("      MESA DE PARTES DIGITAL     ")
    print("---------------------------------")
    print("1. Registrar nuevo expediente")
    print("2. Buscar expediente")
    print("3. Ordenar y mostrar todos")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    return opcion

# ==========================================
# PERSONA 2: Registro de datos
# ==========================================
def registrar_expediente(lista):
    dni = input("Ingresa DNI (8 números): ")
    if len(dni) != 8:
        print("Error: El DNI debe tener 8 números.")
        return # Termina la función aquí mismo si hay error

    nombres = input("Nombres completos: ")
    asunto = input("Asunto del trámite: ")
    
    # Crear código al azar para el expediente
    numero_azar = random.randint(1000, 9999)
    codigo = "EXP-" + str(numero_azar)
    
    # Crear un arreglo (lista) para este expediente
    nuevo_expediente = [codigo, dni, nombres, asunto]
    
    # Agregar a la lista general
    lista.append(nuevo_expediente)
    
    print("Expediente guardado con éxito. Código: " + codigo)
    return nuevo_expediente