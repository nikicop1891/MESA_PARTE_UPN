from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Nombre del archivo de base de datos en texto plano
ARCHIVO_DATOS = "datos.txt"

# ==========================================
# FUNCIONES DE APOYO (LÓGICA Y ARCHIVOS)
# ==========================================
def guardar_en_archivo(expediente):
    """Guarda un nuevo arreglo de expediente en el archivo txt separado por |"""
    with open(ARCHIVO_DATOS, "a", encoding="utf-8") as archivo:
        linea = "|".join(expediente)
        archivo.write(linea + "\n")

def generar_codigo():
    """Busca el número de expediente más alto y genera el correlativo siguiente"""
    if not os.path.exists(ARCHIVO_DATOS):
        return "EXP-0001"
        
    numero_maximo = 0
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split("|")
            if len(datos) == 11:
                # Extrae el número (ej. "0001" de "EXP-0001") y busca el mayor
                try:
                    numero_actual = int(datos[0].split("-")[1])
                    if numero_actual > numero_maximo:
                        numero_maximo = numero_actual
                except:
                    pass
                    
    nuevo_numero = numero_maximo + 1
    return f"EXP-{nuevo_numero:04d}"

# ==========================================
# RUTAS WEB (CONTROLADORES FLASK)
# ==========================================

# 1. Ruta Principal: Formulario de Registro
@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        # Capturamos los datos enviados desde registrar.html
        dni = request.form.get("dni", "").strip()
        tipo = request.form.get("tipo", "Persona Natural")
        nombres = request.form.get("nombres", "").strip()
        asunto = request.form.get("asunto", "").strip()
        
        # Generamos el código único para este registro
        codigo = generar_codigo()
        
        # Estructuramos el arreglo con los 11 campos requeridos
        # (Los campos que no están en el HTML inicial se rellenan por defecto)
        nuevo_expediente = [
            codigo, 
            dni, 
            tipo, 
            nombres, 
            "Dirección no especificada", 
            "correo@ejemplo.com", 
            "000-0000", 
            asunto, 
            "Descripción omitida", 
            "Sin adjuntos", 
            "Pendiente"
        ]
        
        # Persistencia de los datos
        guardar_en_archivo(nuevo_expediente)
        mensaje = f"¡Expediente guardado con éxito! Código asignado: {codigo}"
        
    return render_template("registrar.html", mensaje=mensaje)


# 2. Ruta de Búsqueda
@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultados = []
    mensaje = ""
    
    if request.method == "POST":
        # Capturamos el término a buscar (DNI o Código)
        termino = request.form.get("termino", "").strip().upper()
        
        if os.path.exists(ARCHIVO_DATOS):
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split("|")
                    if len(datos) == 11:
                        # Comparamos con el Código (índice 0) o el DNI/RUC (índice 1)
                        if datos[0].upper() == termino or datos[1] == termino:
                            resultados.append(datos)
            
            # Si recorrió todo el archivo y la lista sigue vacía
            if not resultados:
                mensaje = "No se encontró ningún expediente con ese documento o código."
                
    return render_template("buscar.html", resultados=resultados, mensaje=mensaje)


# 3. Ruta de Listado General
@app.route("/listar")
def listar():
    lista_expedientes = []
    
    # Cargamos todos los registros en memoria para enviarlos a la tabla
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 11:
                    lista_expedientes.append(datos)
                    
    # Renderizamos la plantilla listar.html pasándole el arreglo bidimensional
    return render_template("listar.html", expedientes=lista_expedientes)


# ==========================================
# INICIO DEL SERVIDOR
# ==========================================
if __name__ == "__main__":
    # debug=True permite actualizar la web sin tener que reiniciar la consola si haces cambios en el código
    app.run(debug=True)