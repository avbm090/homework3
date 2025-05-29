# Proyecto EcoWatch

## Descripción

Este proyecto es parte de una solución para **EcoWatch**, una empresa de monitoreo ambiental. La solución procesa y gestiona datos generados por sensores ambientales ubicados en distintas ciudades. El sistema recibe datos de temperatura, humedad y niveles de CO2 cada minuto y los procesa para generar reportes diarios, detectar anomalías y tomar decisiones operativas en tiempo real.

El sistema está diseñado para ser modular, eficiente y escalable, utilizando principios de programación orientada a objetos.

## Objetivo

- **Leer y validar los datos de logs** generados por los sensores.
- **Crear un sistema de caché temporal** que guarde los datos de los últimos 5 minutos para consultas rápidas.
- **Generar reportes** Utilizando patrones de diseño como **Factory** y/o **Strategy**.

## Características

- **Lectura y validación de logs**: Se implementa un parser con pandas para cambiar el formato a dataframe o json.
- **Caché temporal**: Los datos se almacenan en memoria para una rápida consulta de los últimos registros de sensores (con ventana de 5 minutos).
- **Reportes**: Se generan reportes de estado por sala, alertas críticas, y consultas de registros por sala y rango de fechas. La solución es extensible para añadir más tipos de reportes en el futuro.
- **Modularidad**: El sistema está diseñado de manera modular para facilitar su mantenimiento y ampliación.

## Estructura del Proyecto

- **`/data/`**: Carpeta que contiene los archivos de datos, caché y los logs de los sensores. Estos archivos se muestran por vez excepcional, ya que son utilizados como parte de la tarea (homework).
  
- **`/jsons/`**: Carpeta que contiene los informes y resultados de las consultas, tanto de reportes generados como de consultas por fecha o por sala. Estos archivos se guardan en formato **JSON** para persistir la información de manera estructurada. Esto también se muestra de manera excepcional a fin de mostrar el labor realizado en la homework.

- **`/reportes/`**: Carpeta que contiene las clases responsables de generar los reportes. Los reportes se implementan utilizando una combinación de los patrones **Factory** y **Strategy**.

- **`/modelos/`**: Contiene las clases que representan las entidades principales del dominio (en este caso, logs). Cada clase encapsula los atributos de los logs.

- **`/tests/`**: Contiene scripts para realizar pruebas del sistema, en este caso para medición de rendimiento general y posible análisisd e cuellos de botella (se utilizó profiling). Los registros de las pruebas se guardan en formato **texto** en esta carpeta.

- **`/validador/`**: Implementa el validador de los logs para rastrear posibles cceldas con valores nulos, esto es externo al main y a la API.

**`/raíz del proyecto/`**: 
- *`API.py`*: Script que implementa una API para realizar consultas de registros por salas y rango de fechas, esta opción se agregó como un plus y funciona de manera paralela al main. Por falta de tiempo, solo se hicieron estos dos endpoints mencionados.
   - Consultas por salas utiliza el método get, esto es porque se quieren recuperar los datos sin modificar el estado del servidor.
   - Consultas entre rango de fechas utiliza un método post, dado que es necesario enviar un json con parámetros específicos para la consulta (en este caso, el rango de fechas para la búsqueda)
- *`Main.py`*: Contiene la estructura principal para la interacción con el usuario, el diseño es simple ys e visualiza por consola. Permite seleccionar el tipo de informe que se desea crear y también la posibilidad de realizar dos tipos de consultas.
  - En este archivo primero se cargan las variables de entorno, después se parsea la tabla de la bbdd (en este caso el archivo de la tarea), luego, se genera una instancia de la clase Cache (con el archivo ya parseado). Luego, aparece el menú por consola. Cabe aclarar que para cad auna de las opciones siempre se recurre al caché en memoria primero.
      - Opción 1: Trae el informe de cantidad de tipos de estados por sala, utilizando el método ReporteFactory.crear_reporte() de Factory, una vez instanciado, se aplica el método .generar() de strategy.Para el tipo de informe seleccionado, strategy utiliza AlertasCriticas(Strategy), es decir una clase que hereda de la calse abstracta generar(). En resumen, se utiliza factory para crear los objetos nuevos  (los informes) teniendo en cuenta el método (acá es donde se combina con strategy) para el tipo de reporte seleccionado.
      - Opción 2: Similar a la opción 1, pero cuando se instancia generar() se utiliza internamente AlertasCriticas(Strategy) para el informe de cantidad e alertas críticas.
      - Opción 3: Realiza una consulta de registros por sala.
      - Opción 4: Realiza una consulta de registros por rango de fechas. El formato ingresado debe ser del tipo yyyy-mm-ddTHH:MM:SS.

## Requisitos

- **Python 3.7** o superior
- Librerías:
  - `fastapi` para crear la API.
  - `pydantic` para validación de datos.
  - `python-dotenv` para manejar variables de entorno.
  - `pandas` para el procesamiento de datos.
  - `uvicorn` como servidor para la API.

Para instalar las librerías:

```bash
pip install -r requirements.txt
