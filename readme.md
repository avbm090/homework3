# Proyecto EcoWatch

## Descripción

Esta homework es parte de una solución para una empresa ficticia **EcoWatch**, de monitoreo ambiental. La solución procesa y gestiona datos generados por sensores ambientales ubicados en distintas ciudades. 
El sistema recibe datos de temperatura, humedad y niveles de CO₂ cada minuto y los procesa para generar reportes diarios, detectar anomalías y tomar decisiones operativas en tiempo real.

El sistema está diseñado para ser modular, eficiente y escalable, utilizando principios de programación orientada a objetos.

## Objetivo

- Leer y validar los datos de logs generados por los sensores, que pueden estar en distintos formatos (CSV, JSON, etc.).
- Crear un sistema de caché temporal que guarde los datos de los últimos 5 minutos para consultas rápidas.
- Generar reportes ejecutivos personalizados para las decisiones del equipo directivo, utilizando patrones de diseño como **Factory** y **Strategy**.

## Características

- **Lectura y validación de logs**: Se implementa un parser para leer logs de sensores en diferentes formatos.
- **Caché temporal**: Los datos se almacenan en memoria para una rápida consulta de los últimos registros de sensores, con una ventana de 5 minutos.
- **Reportes**: Se generan reportes de estado por sala y alertas críticas, entre otros. La solución es extensible para añadir más tipos de reportes en el futuro de manera modular.
- **Modularidad**: El sistema está diseñado de manera modular para facilitar su mantenimiento y ampliación.

## Estructura del Proyecto

- **`/data/`**: Carpeta que contiene los archivos de datos, caché, y los logs de los sensores. Estos archivos se muestran por vez excepcional, teniendo en cuenta que esto es una muestra de una homework.
- **`/reportes/`**: Carpeta que contiene las clases responsables de generar los reportes.
- **`/modelos/`**: Contiene las clases que representan las entidades principales del dominio (por ejemplo, los logs).
- **`/tests/`**: Contiene scripts para realizar pruebas del sistema con profiling.
- **`/validador/`**: Implementa el validador de los logs para asegurarse de que los datos tengan formato correcto.
- **`API.py`**: Script que implementa una API para interactuar con el sistema.

## Requisitos

- **Python 3.7** o superior
- Librerías:
  - `fastapi` para crear la API.
  - `pydantic` para validación de datos.
  - `python-dotenv` para manejar variables de entorno.
  - `pandas` para el procesamiento de datos.
  - `uvicorn` como servidor para la API.

para instalar las librerías:

```bash
pip install -r requirements.txt
