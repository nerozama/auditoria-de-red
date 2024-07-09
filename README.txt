**Informe del Proyecto** 

  

**Introducción** 

  

Este proyecto tiene como objetivo desarrollar una herramienta de auditoría de red que permite escanear direcciones IP, identificar servicios y sistemas operativos, y detectar posibles vulnerabilidades. La herramienta está diseñada para integrarse con una interfaz gráfica de usuario (GUI) que facilita su uso y permite visualizar los resultados del escaneo de manera clara y ordenada. 

  

**Componentes del Proyecto** 

  

### 1. `escan.py` 

  

Este archivo es el núcleo del sistema de escaneo de red. Contiene funciones esenciales para validar direcciones IP y realizar escaneos utilizando Nmap. La validación de la IP asegura que solo se procesen direcciones válidas, y el escaneo de red proporciona detalles sobre los puertos abiertos, servicios en ejecución, y posibles vulnerabilidades. 

  

#### Función de Validación de IP 

  

- **Propósito**: Asegurar que la dirección IP ingresada por el usuario es válida. 

- **Descripción**: Utiliza una expresión regular para verificar que la dirección IP esté en el formato correcto (IPv4). 

- **Uso**: Antes de realizar cualquier escaneo, se verifica la validez de la dirección IP ingresada por el usuario. 

  

#### Función de Escaneo de Red 

  

- **Propósito**: Realizar un escaneo de red utilizando Nmap. 

- **Descripción**: Ejecuta un comando de Nmap que escanea los primeros 1000 puertos, detecta el sistema operativo y los servicios en ejecución, y proporciona un informe detallado. 

- **Uso**: Esta función es invocada después de que se valida la dirección IP, y los resultados del escaneo se muestran en la interfaz de usuario. 

  

### 2. `interfaz.py` 

  

Este archivo contiene la implementación de la interfaz gráfica de usuario (GUI) utilizando la biblioteca Tkinter de Python. La GUI proporciona un entorno interactivo donde los usuarios pueden ingresar direcciones IP, iniciar escaneos, y ver los resultados en tiempo real. 

  

#### Configuración de la Interfaz 

  

- **Propósito**: Crear una ventana de aplicación interactiva y fácil de usar. 

- **Descripción**: La ventana de la aplicación tiene un diseño personalizado, incluyendo colores, fuentes y dimensiones específicas para mejorar la experiencia del usuario. 

- **Uso**: Los usuarios interactúan con la interfaz para iniciar y visualizar los escaneos. Los resultados se muestran en un área de texto desplazable. 

  

#### Función de Confirmación 

  

- **Propósito**: Iniciar el escaneo y mostrar los resultados. 

- **Descripción**: Esta función se ejecuta cuando el usuario presiona el botón de "Confirmar". Valida la dirección IP ingresada, inicia el escaneo utilizando Nmap, y muestra los resultados en el área de texto. 

- **Uso**: Los usuarios pueden ver los resultados del escaneo en tiempo real, línea por línea, mientras se ejecuta el comando Nmap. 

  

### 3. `main.py` 

  

Este archivo integra las funciones de `escan.py` y `interfaz.py`, proporcionando una entrada unificada para ejecutar el programa. También incluye una función para consultar vulnerabilidades específicas utilizando el identificador CVE. 

  

#### Función Principal 

  

- **Propósito**: Coordinar la ejecución del escaneo y la consulta de vulnerabilidades. 

- **Descripción**: Llama a las funciones de escaneo y consulta de vulnerabilidades, gestionando la lógica de flujo del programa. 

- **Uso**: Este archivo puede ser ejecutado directamente para iniciar el programa, y maneja la interacción entre la consola y la interfaz gráfica. 

  

#### Consulta de Vulnerabilidades por CVE 

  

- **Propósito**: Obtener detalles de vulnerabilidades específicas. 

- **Descripción**: Realiza una solicitud a la API de la NVD (National Vulnerability Database) para obtener información detallada sobre una vulnerabilidad utilizando su identificador CVE. 

- **Uso**: Puede ser utilizado para mostrar detalles adicionales sobre vulnerabilidades detectadas durante el escaneo. 

  

## Uso del Programa 

  

### Preparación 

  

1. **Instalación de Nmap**: Asegúrese de tener Nmap instalado en la ruta especificada (por defecto, "C:\\Program Files (x86)\\Nmap\\nmap.exe"). 

2. **Dependencias**: Instale las bibliotecas necesarias utilizando `pip` (e.g., Tkinter, Requests). 

  

### Ejecución 

  

1. **Inicio del Programa**: Ejecute el archivo `main.py` para iniciar el programa. 

2. **Ingreso de Dirección IP**: Ingrese una dirección IP válida en la interfaz gráfica. 

3. **Iniciar Escaneo**: Presione el botón "Confirmar" para iniciar el escaneo. 

4. **Visualización de Resultados**: Los resultados del escaneo se mostrarán en el área de texto desplazable de la GUI. 

5. **Consulta de Vulnerabilidades**: Opcionalmente, consulte detalles de vulnerabilidades específicas utilizando el identificador CVE. 

  

### Casos de Uso 

  

- **Auditoría de Seguridad**: Realice auditorías de seguridad en redes para identificar puertos abiertos, servicios vulnerables y sistemas operativos. 

- **Evaluación de Vulnerabilidades**: Consulte detalles específicos de vulnerabilidades conocidas para evaluar riesgos. 

- **Generación de Informes**: Utilice los resultados del escaneo para generar informes detallados sobre el estado de la seguridad de la red. 

  

## Conclusión 

  

Este proyecto proporciona una herramienta completa para la auditoría de redes, combinando la potencia de Nmap con una interfaz gráfica amigable. Su capacidad para realizar escaneos detallados y consultar vulnerabilidades conocidas lo convierte en una herramienta valiosa para cualquier profesional de la ciberseguridad. 

  

--- 