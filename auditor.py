#auditor
import subprocess
import re
from scanner import realizar_escaneo  # Importa la función de escaneo

def validar_ip(address):
    """
    Valida si una dirección IP es válida.

    Args:
    address (str): Dirección IP a validar.

    Returns:
    bool: True si es válida, False si no lo es.
    """
    patron = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return patron.match(address) is not None

def main(address=None):
    """
    Función principal para ejecutar el escaneo y consultar vulnerabilidades.

    Args:
    address (str, optional): Dirección IP a escanear. Si no se proporciona, se solicitará al usuario.
    """
    if address is None:
        address = input("Ingrese la dirección IP que desea escanear: ")

    if validar_ip(address):
        realizar_escaneo(address)
    else:
        print("Dirección IP no válida.")

if __name__ == "__main__":
    main()
