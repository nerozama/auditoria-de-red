#scanner
import os
import re
import subprocess
import threading

def validar_ip(address):
    """
    Valida si una dirección IP tiene un formato correcto.

    Args:
    address (str): Dirección IP a validar.

    Returns:
    bool: True si la dirección IP es válida, False en caso contrario.
    """
    patron = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return patron.match(address) is not None

def crear_directorios(base_path):
    """
    Crea los directorios necesarios para guardar los resultados de los escaneos.

    Args:
    base_path (str): Ruta base donde crear los directorios.
    """
    try:
        os.makedirs(os.path.join(base_path, "nmap"), exist_ok=True)
        os.makedirs(os.path.join(base_path, "content"), exist_ok=True)
        os.makedirs(os.path.join(base_path, "exploits"), exist_ok=True)
    except Exception as e:
        print(f"Error al crear los directorios: {e}")

def realizar_escaneo(address):
    """
    Realiza un escaneo de red usando Nmap de manera asincrónica.

    Args:
    address (str): Dirección IP a escanear.
    """
    if not validar_ip(address):
        print("Dirección IP no válida.")
        return

    try:
        # Ruta base donde crear los directorios
        base_path = r"C:\Users\nero\Documents\vscode\auditorias"

        # Crear los directorios necesarios
        crear_directorios(base_path)

        # Cambiar al directorio nmap
        os.chdir(os.path.join(base_path, "nmap"))

        # Lista de argumentos para el comando de Nmap
        nmap_args = [
            "C:\\Program Files (x86)\\Nmap\\nmap.exe",
            "-sS",       # Escaneo de tipo SYN
            "-O",        # Detección de sistema operativo
            "-sV",       # Detección de versiones de servicios
            "-p-",       # Escanear todos los puertos (0-65535)
            "--open",    # Mostrar solo puertos abiertos
            "-T4",       # Velocidad de escaneo rápida
            "-vvv",      # Modo verbose para obtener más detalles
            "-A",        # Activar la detección de SO, versión y scripts de escaneo
            address      # Dirección IP a escanear, añadida al final de la lista
        ]

        # Ejecutar el comando Nmap de manera asincrónica
        def ejecutar_nmap():
            try:
                subprocess.Popen(nmap_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except Exception as e:
                print(f"Error al ejecutar nmap de manera asincrónica: {e}")

        # Crear un hilo para ejecutar Nmap de manera asincrónica
        nmap_thread = threading.Thread(target=ejecutar_nmap)
        nmap_thread.start()

        # Esperar al hilo principal sin bloquear la interfaz
        nmap_thread.join()

        print("Escaneo iniciado en segundo plano. Consulte los resultados en el directorio nmap.")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
