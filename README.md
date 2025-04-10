Instalación y Ejecución

1.  Clonar o descargar el repositorio
    Clona el repositorio con:
    ```bash
    git clone https://github.com/migueltorresv/transactions_interbank_codeable.git
    ```
    o descarga el código en formato ZIP y descomprímelo en una carpeta.
2.  Navegar al directorio del proyecto
    ```bash
    git clone https://github.com/migueltorresv/transactions_interbank_codeable.git
    ```
    cd transactions_interbank_codeable
3.  Verificar la existencia de los archivos principales
    Asegúrate de contar con el archivo del script (transactions.py) y tu archivo CSV de transacciones (por ejemplo, transacciones.csv).
4.  Ejecutar la aplicación
    Abre la terminal y ejecuta:
    ```bash
    python transactions.py transacciones.csv
    ```
    La aplicación leerá el archivo CSV y mostrará un reporte similar al siguiente:
    ```bash
    Reporte de Transacciones
    ---------------------------------------------
    Balance Final: 325.00
    Transacción de Mayor Monto: ID 3 - 200.00
    Conteo de Transacciones: Crédito: 3 Débito: 2
    ```
Enfoque y Solución

La solución se basa en una estructura simple y eficiente:

    Lectura del CSV: Se utiliza csv.DictReader para procesar el archivo línea por línea, lo que permite trabajar con archivos de gran tamaño sin sobrecargar la memoria.

    Procesamiento de Datos: Se recorren las transacciones, actualizando el balance, identificando la transacción con el mayor monto y contando las transacciones de cada tipo.

    Interfaz de Línea de Comandos (CLI): Con argparse, la aplicación recibe como argumento la ruta del archivo CSV, facilitando su ejecución desde la terminal.
Las decisiones de diseño se han centrado en la simplicidad, la legibilidad del código y la eficiencia en el procesamiento de archivos.