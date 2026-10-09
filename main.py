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

# ==========================================
# PERSONA 3: Archivos y Búsqueda
# ==========================================
def guardar_en_archivo(expediente):
    # Abrir el archivo de texto en modo "a" (agregar al final)
    archivo = open("datos.txt", "a") 
    linea = expediente[0] + "," + expediente[1] + "," + expediente[2] + "," + expediente[3]
    archivo.write(linea + "\n")
    archivo.close()

def cargar_datos(lista):
    try:
        # Abrir el archivo de texto en modo "r" (leer)
        archivo = open("datos.txt", "r") 
        lineas = archivo.readlines()
        for linea in lineas:
            # Limpiar el salto de línea (Enter) y separar por comas
            linea_limpia = linea.replace("\n", "")
            datos = linea_limpia.split(",")
            lista.append(datos)
        archivo.close()
    except FileNotFoundError:
        # Si el archivo no existe (es la primera vez que se abre el programa), no hace nada
        pass

def buscar_expediente(lista):
    codigo_buscar = input("Ingresa el código a buscar (ej. EXP-1234): ")
    
    for exp in lista:
        if exp[0] == codigo_buscar:
            print("\n--- EXPEDIENTE ENCONTRADO ---")
            print("Código: " + exp[0])
            print("DNI: " + exp[1])
            print("Nombres: " + exp[2])
            print("Asunto: " + exp[3])
            return # Termina la búsqueda porque ya lo encontró
            
    print("\nNo existe ese código.")