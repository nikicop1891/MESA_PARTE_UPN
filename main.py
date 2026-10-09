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