from reportes.factory import ReporteFactory
from logs.log_config import logger
from dotenv import load_dotenv
import os
from datetime import datetime
from data.cache.cache import Cache
from data.parsers.parser import LogParser




def main():
    load_dotenv()
    csv_path = os.getenv("CSV_PATH")
    
    parser = LogParser(csv_path)
    try:
        df_logs = parser.parse_csv_a_logs()
        logger.info("Archivo CSV cargado y parseado con Log correctamente.")
    except Exception as e:
        logger.error(f"No se pudo cargar o parsear el archivo CSV: {e}")
        print(f"Error de carga de archivo: {e}")
        return
    
    cache = Cache(df_logs)

    while True:
        print("Reportes y consultas:")
        print("1. reporte: estado por sala")
        print("2. reporte: alertas críticas")
        print("3. consulta logs por sala")
        print("4. consulta logs por fecha")
        print("s. salir")

        
        opcion_numero = input("Ingresar tipo de reporte ").strip()

        if opcion_numero == "1":
            logger.info(f"reporte seleccionado: estado por sala.")
            sala = input("Ingresar nombre de sala ").strip()
            try:
                reporte = ReporteFactory.crear_reporte("estado_sala")
                reporte.generar(df_logs, sala)
                logger.info("reporte de estado por sala generado ok.")
            except Exception as e:
                logger.error(f"error al generar el reporte estado por sala: {e}")

        elif opcion_numero == "2":
            logger.info(f"reporte seleccionado: cantidad de alertas críticas")
            try:
                reporte = ReporteFactory.crear_reporte("alertas_criticas")
                reporte.generar(df_logs, None)
                logger.info("reporte de cantidad de alertas críticas generado ok.")
            except Exception as e:
                logger.error(f"error al generar el reporte alertas críticas: {e}")

        elif opcion_numero == "3":
            sala = input("consulta por sala: ").strip()
            try:
                df_filtrado = cache.consulta_por_sala(sala)
                if df_filtrado.empty:
                    print("no hay registros.")
                else:
                    print(df_filtrado.to_string(index=False))
                logger.info(f"consulta rápida por sala '{sala}' ok.")
            except Exception as e:
                logger.error(f"error en consulta rápida por sala: {e}")

        elif opcion_numero == "4":
            try:
                desde_str = input("Fecha y hora desde (yyyy-mm-ddTHH:MM:SS): ").strip()
                hasta_str = input("Fecha y hora hasta (yyyy-mm-ddTHH:MM:SS): ").strip()
                desde = datetime.strptime(desde_str, "%Y-%m-%dT%H:%M:%S")
                hasta = datetime.strptime(hasta_str, "%Y-%m-%dT%H:%M:%S")

                df_filtrado = cache.consulta_por_timestamp(desde, hasta)

                if df_filtrado.empty:
                    print("No hay registros en ese rango de fechas.")
                else:
                    print(df_filtrado.to_string(index=False))

                logger.info("consulta rápida por rango de tiempo realizada.")
            except Exception as e:
                logger.error(f"error en consulta rápida por rango de tiempo: {e}")

        elif opcion_numero == "s":
            print("saliendo...")
            break 

        else:
            logger.warning(f"opción ingresada no válida : {opcion_numero}")
            print("Ingresar una opción válida.")

            

if __name__ == "__main__":
    main()
