# PyUSBTool - USB Formatter

![PyUSBTool](https://img.shields.io/badge/Version-1.0-blue.svg) 

**PyUSBTool** es una herramienta sencilla pero poderosa para formatear unidades USB desde la terminal. Con esta aplicación, puedes listar tus unidades USB conectadas, seleccionar una para formatear y eliminar todos los datos en ella. El proceso incluye una advertencia y una barra de progreso visual durante la operación de formateo.

## Características

- **Listado de Dispositivos USB Conectados**: Muestra las unidades USB actualmente conectadas.
- **Confirmación de Formateo**: Antes de borrar los datos, el programa te pedirá confirmación para evitar accidentes.
- **Barra de Progreso**: Muestra un progreso visual durante el formateo de la unidad seleccionada.
- **Interfaz de Usuario Sencilla**: Utiliza colores para resaltar los mensajes importantes y errores.

## Requisitos

Para ejecutar esta herramienta, necesitarás tener instalados algunos módulos de Python y dependencias del sistema. A continuación, se detallan las instrucciones de instalación.

### Requisitos del Sistema

Asegúrate de tener las siguientes herramientas instaladas:

- **Python 3.x**: Esta herramienta está escrita en Python 3.
- **psutil**: Para interactuar con las particiones y discos del sistema.
- **progressbar**: Para la barra de progreso durante el formateo.

### Instalación

Sigue estos pasos para instalar los módulos necesarios y ejecutar el proyecto:

1. **Clona el repositorio o descarga los archivos del proyecto:**

   ```bash
   git clone https://github.com/i-100-user/PyUSBTool.git
   cd PyUSBTool
   ```

2. **Instala las dependencias necesarias:**

   Primero, asegúrate de tener los paquetes necesarios instalados utilizando `apt` para las dependencias del sistema:

   ```bash
   sudo apt update
   sudo apt install python3-psutil python3-progressbar
   ```

   Esto instalará las bibliotecas de Python requeridas (`psutil` y `progressbar`) en tu sistema.

3. **Ejecuta el programa:**

   Asegúrate de tener permisos de superusuario, ya que se necesitan para desmontar y formatear las unidades USB. Para ejecutar el script:

   ```bash
   sudo python3 PyUSBTool.py
   ```

   El programa te pedirá que elijas el dispositivo USB que deseas formatear, confirmes la acción y luego procederá a formatearlo.

### Uso

1. **Listado de Dispositivos USB**: El programa te mostrará una lista de las unidades USB conectadas a tu sistema.
   
2. **Seleccionar Dispositivo**: Elige el número del dispositivo que deseas formatear.

3. **Confirmación de Formateo**: Se te pedirá una confirmación para proceder con el formateo. Asegúrate de que realmente deseas borrar los datos.

4. **Progreso del Formateo**: Mientras el dispositivo se formatea, verás una barra de progreso que muestra el estado del proceso.

5. **Error o Éxito**: Al finalizar, el programa te informará si el formateo fue exitoso o si ocurrió algún error.

---

### Contribuciones

Si tienes alguna mejora o corrección, no dudes en crear un "pull request" o reportar un "issue". ¡Gracias por tu contribución!

---

¡Disfruta de **PyUSBTool** y mantén tus unidades USB siempre organizadas y limpias! 😎
