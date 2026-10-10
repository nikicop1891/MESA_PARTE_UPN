def mostrar_menu():
    print("\n" * 2) 
    print("==================================================")
    print("              MESA DE PARTES DIGITAL              ")
    print("==================================================")
    print("¡Hola! Revisa la fecha de recepción de documentos")
    print("según el art. 46.2 del Decreto Supremo N.° 075-2023-PCM:")
    print(" - Desde las 00:00 hasta las 18:00 hrs: Se consideran")
    print("   recibidos el mismo día.")
    print(" - Después de las 18:00 hasta las 23:59 hrs: Cuentan")
    print("   desde el día hábil siguiente.")
    print(" - Sábados, domingos y feriados: Cuentan desde el")
    print("   día hábil siguiente.")
    print("--------------------------------------------------")
    print("1. Registrar nuevo expediente")
    print("2. Buscar por Documento o Código")
    print("3. Ordenar y mostrar todos")
    print("4. Actualizar estado del trámite")
    print("5. Anular expediente (Eliminar)")
    print("6. Reporte estadístico gerencial")
    print("7. Salir")
    print("==================================================")
    opcion = input("Elige una opción: ").strip() 
    return opcion

def actualizar_estado(lista):
    codigo_buscar = input("Ingresa el Código del expediente a actualizar (Ej: EXP-0001): ").upper().strip()
    encontrado = False
    
    for exp in lista:
        if exp[0] == codigo_buscar:
            print("\nTrámite encontrado : " + exp[3] + " - " + exp[7])
            print("Estado actual      : [" + exp[10] + "]")
            print("\nNuevos estados disponibles:")
            print("A) En revisión")
            print("B) Observado (Falta información)")
            print("C) Atendido (Finalizado)")
            nuevo = input("Elige el nuevo estado (A, B o C): ").upper().strip()
            
            if nuevo == "A":
                exp[10] = "En revisión"
            elif nuevo == "B":
                exp[10] = "Observado"
            elif nuevo == "C":
                exp[10] = "Atendido"
            else:
                print("Opción inválida. No se cambió el estado.")
                return
                
            print("¡Estado actualizado correctamente a: " + exp[10] + "!")
            reescribir_archivo(lista) 
            encontrado = True
            break 
            
    if encontrado == False:
        print("No se encontró ningún expediente con ese código.")

def anular_expediente(lista):
    codigo_buscar = input("Ingresa el Código del expediente a ELIMINAR (Ej: EXP-0001): ").upper().strip()
    
    for exp in lista:
        if exp[0] == codigo_buscar:
            print("\nTrámite a eliminar : " + exp[3] + " - " + exp[7])
            confirmacion = input("¿Estás seguro de anular este expediente? (S/N): ").upper().strip()
            
            if confirmacion == "S":
                lista.remove(exp)
                reescribir_archivo(lista)
                print("¡Expediente " + codigo_buscar + " anulado y eliminado del sistema exitosamente!")
            else:
                print("Operación cancelada. El expediente no fue eliminado.")
            return # Termina la función
            
    print("No se encontró ningún expediente con ese código para eliminar.")