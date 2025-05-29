# Proyecto EcoWatch

## Descripción

Este proyecto es parte de una homework, se porpone una solución para una empresa ficticia **EcoWatch**, de monitoreo ambiental. La solución procesa y gestiona datos generados por sensores ambientales ubicados en distintas ciudades. El sistema recibe datos de temperatura, humedad y niveles de CO2 cada minuto y los procesa para generar reportes diarios, detectar anomalías y tomar decisiones operativas en tiempo real.

El sistema está diseñado para ser modular, eficiente y escalable, utilizando principios de programación orientada a objetos.

## Objetivo

- **Leer y validar los datos de logs** generados por los sensores.
- **Crear un sistema de caché temporal** que guarde los datos de los últimos 5 minutos para consultas rápidas.
- **Generar reportes** Utilizando patrones de diseño como **Factory** y/o **Strategy**.

## Características

- **Lectura y logs**: Se implementa un **parser** utilizando **pandas** para convertir los datos a un formato **DataFrame** o **JSON**, facilitando su manipulación y exportación. Además, el sistema de **registro de logs** utiliza la librería **logging**, que permite registrar eventos importantes del sistema y guardarlos en un archivo de texto (.txt).
- **Caché temporal**: Los datos se almacenan en memoria para una rápida consulta de los últimos registros de sensores (con ventana de 5 minutos).
- **Reportes**: Se generan reportes de estado por sala, alertas críticas, y consultas de registros por sala y rango de fechas. La solución es extensible para añadir más tipos de reportes en el futuro.
- **Modularidad**: El sistema está diseñado de manera modular para facilitar su mantenimiento y ampliación.

## Estructura del Proyecto

- **`/data/`**: Carpeta que contiene los archivos de datos, caché y los logs de los sensores. **Estos archivos se muestran por vez excepcional**, ya que son utilizados como parte de la tarea (homework).
  
- **`/jsons/`**: Carpeta que contiene los informes y resultados de las consultas hechas desde la API, tanto de reportes generados como de consultas por fecha o por sala. Estos archivos se guardan en formato **JSON** para persistir la información de manera estructurada. **Esto también se muestra de manera excepcional a fin de mostrar el labor realizado en la homework**.

- **`/logs/`**: Carpeta donde se almacenan lso registros generados por la aplicación. Genera un registro en formatos .txt. Tipos: 'INFO' para eventos informativos, 'WARNING' para advertencias y 'ERROR' para situaciones que requieren corrección. **Estos archivos se muestran por vez excepcional**.

- **`/reportes/`**: Carpeta que contiene las clases responsables de generar los reportes. Los reportes se implementan utilizando una combinación de los patrones **Factory** y **Strategy**.

- **`/modelos/`**: Contiene las clases que representan las entidades principales del dominio (en este caso, logs). Cada clase encapsula los atributos de los logs.

- **`/tests/`**: Contiene scripts para realizar pruebas del sistema, en este caso para medición de rendimiento general y posible análisisd e cuellos de botella (se utilizó profiling). Los registros de las pruebas se guardan en formato **texto** en esta carpeta.

- **`/validador/`**: Implementa el validador de los logs para rastrear posibles cceldas con valores nulos, esto es externo al main y a la API.

Archivos principales en **`/homework3/`**: 
- *`API.py`*: Script que implementa una API para realizar consultas de registros por salas y rango de fechas, esta opción se agregó como un plus, y funciona de manera paralela al main. Por falta de tiempo, solo se hicieron estos dos endpoints mencionados.
   - Consultas por salas: La consulta por sala utiliza el método GET, ya que sólo recupera datos sin modificar el estado del servidor.
   - Consultas entre rango de fechas: La consulta por rango de fechas utiliza el método POST, porque se envía un JSON con parámetros específicos (el rango de fechas) para realizar la búsqueda.
- *`Main.py`*: Contiene la estructura principal. Acá es donde se selecciona el tipo de informe a través de una interfaz por consola. Principalemnte lo que se hace en este archivo es:
  1. Se cargan las **variables de entorno**.
  2. Se **parsea** la tabla de la base de datos (en este caso, el archivo de la tarea).
  3. Se genera una instancia de la clase **Cache** con el archivo ya parseado.
  4. Se muestra **menú por consola**, con las opciones para seleccionar el **tipo de informe** o **consulta**.
  
  Cabe aclarar que, para cada una de las opciones, siempre se recurre al **caché en memoria primero**. Es decir, la instancia del caché se crea una sola vez fuera del bucle principal (while) antes que el usuario 
  seleccione alguna opción. Cuando el usuario elige una opción, recién ahí se carga el caché.

  #### **Opciones del menú**:
  - **Opción 1**: Trae el informe de cantidad de tipos de estados por sala, utilizando el método `ReporteFactory.crear_reporte()` del patrón **Factory**. Una vez instanciado el objeto, se aplica el método `.generar()` del patrón **Strategy**. Para el tipo de informe seleccionado, **Strategy** utiliza `EstadoSala(Strategy)`, es decir, una clase que implementa el método `generar()` de la clase abstracta.  
    - En resumen, **Factory** se encarga de crear los objetos de reporte, y dependiendo del tipo de reporte seleccionado, el patrón **Strategy** define cómo se generará el informe, utilizando la lógica de `EstadoSala` para el informe de estados por sala.

  - **Opción 2**: Similar a la opción 1, pero cuando se instancia el método `.generar()`, se utiliza internamente `AlertasCriticas(Strategy)` para el informe de cantidad de alertas críticas.

  - **Opción 3**: Realiza una consulta de registros por sala, consultando el caché en memoria.

  - **Opción 4**: Realiza una consulta de registros por rango de fechas. El formato ingresado debe ser del tipo `yyyy-mm-ddTHH:MM:SS`.
## Requisitos

- **Python 3.7** en adelante
- Requirements:
  - `fastapi` para crear la API.
  - `pydantic` para validación de datos.
  - `python-dotenv` para manejar variables de entorno.
  - `pandas` para el procesamiento de datos.
  - `uvicorn` como servidor para la API.

Instalación de librerías:

En powershell o bash,
pip install -r requirements.txt

  #### **Ejecución**:
  Se corre el archivo main.py para interfaz por consola o el archivo API.py en local para ver la API. 


  ## Mejoras

Aunque el proyecto está en su versión actual, **quedaron pendientes varias mejoras** que podrían haberse implementado con más tiempo:

1. **Agregar más endpoints a la API:**
   - Se planeaba añadir al menos dos endpoints más a la API, que generen lso reportes, así como se hace en main.py. 

2. **Crear una base de datos con MySQL:**
   - En lugar de almacenar la información en el mismo formato que lo recibimoss (csv), se había considerado implementar una **base de datos MySQL**. 
   - Esto se hubiera hecho creando tablas con **MySQL Workbench**, lo que permitiría una gestión más robusta y escalable de los datos.

3. **Integración con variables de entorno:**
   - **Configuración de la conexión a la base de datos:** Se habría configurado la conexión a MySQL utilizando variables de entorno para asegurar que las credenciales y configuraciones no estuvieran expuestas en el código.
   - Las variables de entorno habrían sido almacenadas en un archivo `.env`, para mantener la seguridad y flexibilidad de la configuración de la aplicación.


