import shutil
import datetime
import os
import logging

# Configuración de logs
logging.basicConfig(filename='backup_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def realizar_respaldo(origen, destino):
    """
    Comprime y respalda una carpeta crítica agregando fecha al nombre.
    """
    try:
        # Verificar que la fuente existe
        if not os.path.exists(origen):
            raise FileNotFoundError(f"La carpeta de origen {origen} no existe.")

        # Generar nombre con fecha
        fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        nombre_archivo = f"Respaldo_Clientes_{fecha_hoy}"
        ruta_completa = os.path.join(destino, nombre_archivo)

        print(f"[*] Iniciando respaldo de {origen}...")
        
        # Crear archivo ZIP
        shutil.make_archive(ruta_completa, 'zip', origen)
        
        mensaje = f"Respaldo exitoso: {ruta_completa}.zip"
        print(mensaje)
        logging.info(mensaje)
        
    except Exception as e:
        error_msg = f"Error durante el respaldo: {str(e)}"
        print(error_msg)
        logging.error(error_msg)

if __name__ == "__main__":
    # En un entorno real, estas rutas serían del servidor
    CARPETA_CRITICA = "./Datos_Sensibles"  
    CARPETA_DESTINO = "./Backups"
    
    # Crear carpetas dummy para la demostración si no existen
    if not os.path.exists(CARPETA_CRITICA):
        os.makedirs(CARPETA_CRITICA)
        with open(f"{CARPETA_CRITICA}/clientes.txt", "w") as f:
            f.write("Datos dummy para prueba de respaldo.")
            
    if not os.path.exists(CARPETA_DESTINO):
        os.makedirs(CARPETA_DESTINO)

    # Ejecutar función
    realizar_respaldo(CARPETA_CRITICA, CARPETA_DESTINO)