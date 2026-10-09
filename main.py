import os
import random

ARCHIVO_DATOS = "expedientes.txt"

# ==========================================
# PERSONA 1: Integrador y Menú Principal
# Rol: Lógica de bucles (while/for), menú interactivo e integración del programa.
# ==========================================
def mostrar_menu():
    print("\n" + "="*35)
    print("MUNICIPALIDAD - MESA DE PARTES DIGITAL")
    print("="*35)
    print("1. Registrar nuevo expediente")
    print("2. Buscar expediente por código")
    print("3. Mostrar expedientes (Ordenados por DNI)")
    print("4. Salir")
    return input("Seleccione una opción: ")

def main():
    # Cargar datos al iniciar el programa
    expedientes_memoria = cargar_datos()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            nuevo = registrar_expediente(expedientes_memoria)
            if nuevo:
                guardar_en_archivo(nuevo)
        elif opcion == '2':
            buscar_expediente(expedientes_memoria)
        elif opcion == '3':
            ordenar_y_mostrar(expedientes_memoria)
        elif opcion == '4':
            print("Saliendo del sistema de Mesa de Partes...")
            break
        else:
            print("Error: Opción inválida. Intente nuevamente.")

# ==========================================
# PERSONA 2: Lógica de Registro y Arreglos
# Rol: Captura de datos, validación (condicionales) y manejo de listas.
# ==========================================
def validar_dni(dni):
    return len(dni) == 8 and dni.isdigit()

def registrar_expediente(lista_expedientes):
    print("\n--- NUEVO REGISTRO ---")
    dni = input("Ingrese DNI del ciudadano (8 dígitos): ")
    if not validar_dni(dni):
        print("Error: El DNI ingresado no es válido.")
        return None

    nombres = input("Nombres y Apellidos: ")
    asunto = input("Asunto del trámite: ")
    
    # Generar código único usando cadenas de caracteres
    codigo = f"EXP-{random.randint(1000, 9999)}"
    
    # Estructura lineal (Arreglo unidimensional)
    nuevo_expediente = [codigo, dni, nombres, asunto]
    lista_expedientes.append(nuevo_expediente)
    
    print(f"\n¡Éxito! Expediente registrado correctamente con el código: {codigo}")
    return nuevo_expediente

# ==========================================
# PERSONA 3: Persistencia de Datos y Búsqueda
# Rol: Lectura/escritura de archivos .txt y algoritmos de búsqueda.
# ==========================================
def guardar_en_archivo(expediente):
    # Se abre el archivo en modo append ("a") para no sobreescribir lo anterior
    with open(ARCHIVO_DATOS, "a", encoding="utf-8") as archivo:
        linea = ",".join(expediente)
        archivo.write(linea + "\n")

def cargar_datos():
    lista_expedientes = []
    if not os.path.exists(ARCHIVO_DATOS):
        return lista_expedientes
    # Se lee el archivo de texto y se carga en el arreglo bidimensional
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 4:
                lista_expedientes.append(datos)
    return lista_expedientes

def buscar_expediente(lista_expedientes):
    codigo_buscar = input("\nIngrese el código del expediente (ej. EXP-1234): ").strip()
    
    # Búsqueda iterativa en el arreglo bidimensional
    for exp in lista_expedientes:
        if exp[0].upper() == codigo_buscar.upper():
            print("\n--- EXPEDIENTE ENCONTRADO ---")
            print(f"Código : {exp[0]}\nDNI    : {exp[1]}\nNombres: {exp[2]}\nAsunto : {exp[3]}")
            return
            
    print("No se encontró ningún expediente con ese código.")

# ==========================================
# PERSONA 4: Algoritmos de Ordenamiento
# Rol: Ordenamiento de arreglos bidimensionales (Método Burbuja).
# ==========================================
def ordenar_y_mostrar(lista_expedientes):
    if not lista_expedientes:
        print("No hay expedientes registrados actualmente.")
        return
    
    # Copiamos la lista para no alterar el orden de ingreso original
    lista_ordenada = lista_expedientes.copy()
    n = len(lista_ordenada)
    
    # Algoritmo de Burbuja: Ordenar alfabéticamente por DNI (Índice 1)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_ordenada[j][1] > lista_ordenada[j+1][1]:
                # Intercambio de posiciones
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
    
    print("\n--- EXPEDIENTES REGISTRADOS (Ordenados por DNI) ---")
    for exp in lista_ordenada:
        print(f"[{exp[0]}] DNI: {exp[1]} | {exp[2]} | Asunto: {exp[3]}")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    main()