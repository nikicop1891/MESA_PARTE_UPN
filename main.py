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


# ==========================================
def registrar_expediente(lista):
    print("\n--- DATOS DEL SOLICITANTE ---")
    tipo = input("Tipo de persona (1: Natural, 2: Jurídica): ").strip()
    tipo_persona = "Persona Natural" if tipo == "1" else "Persona Jurídica"
    
    documento = input("Ingresa DNI (8 dígitos) o RUC (11 dígitos): ").strip()
    if len(documento) != 8 and len(documento) != 11:
        print("Error: El documento debe tener 8 u 11 dígitos.")
        return None

    nombres = input("Nombres y apellidos (o Razón social): ").strip()
    direccion = input("Dirección actual: ").strip()
    correo = input("Correo electrónico de contacto: ").strip()
    telefono = input("Teléfono o celular de contacto: ").strip()
    
    print("\n--- DESCRIPCIÓN DEL TRÁMITE ---")
    asunto = input("Asunto de la solicitud: ").strip()
    descripcion = input("Descripción detallada: ").strip()
    
    print("\n--- DOCUMENTOS DE SUSTENTO ---")
    print("(Opcional: Si el archivo pesa más de 10 MB, deja un link de descarga)")
    sustento = input("Link o ruta del documento (Presiona Enter para omitir): ").strip()
    if sustento == "":
        sustento = "Sin documentos adjuntos"
        
    estado_inicial = "Pendiente"
    
    # Búsqueda del número máximo para evitar duplicados
    if len(lista) == 0:
        codigo = "EXP-0001"
    else:
        numero_maximo = 0
        for exp in lista:
            numero_actual = int(exp[0].split("-")[1])
            if numero_actual > numero_maximo:
                numero_maximo = numero_actual
                
        codigo = "EXP-" + str(numero_maximo + 1).zfill(4) 
    
    nuevo_expediente = [
        codigo, documento, tipo_persona, nombres, direccion, 
        correo, telefono, asunto, descripcion, sustento, estado_inicial
    ]
    
    lista.append(nuevo_expediente)
    print("\n¡Expediente guardado con éxito! Código asignado: " + codigo)
    return nuevo_expediente

def reporte_estadistico(lista):
    total = len(lista)
    naturales = 0
    juridicas = 0
    
    for exp in lista:
        if exp[2] == "Persona Natural":
            naturales += 1
        elif exp[2] == "Persona Jurídica":
            juridicas += 1
            
    print("\n--- REPORTE ESTADÍSTICO GERENCIAL ---")
    print("Total de expedientes registrados : " + str(total))
    print("Trámites de Persona Natural      : " + str(naturales))
    print("Trámites de Persona Jurídica     : " + str(juridicas))
    print("---------------------------------------")

# ==========================================
