from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os
from dotenv import load_dotenv
from data.parsers.parser import LogParser
from data.cache.cache import Cache
from logs.log_config import logger
import traceback


app = FastAPI()

load_dotenv()
csv_path = os.getenv("CSV_PATH")

try:
    parser = LogParser(csv_path)
    df_logs = parser.parse_csv_a_logs()
    cache = Cache(df_logs)
    logger.info("carga csv OK.")
except Exception as e:
    logger.error(f"error con cache o carga de csv: {e}")
    raise RuntimeError("error en carga de la API.") from e

if not os.path.exists("jsons"):
    os.makedirs("jsons")
    logger.info("carpeta jsons creada.")

class FechaRango(BaseModel):
    desde: datetime
    hasta: datetime

import traceback


@app.get("/consulta-sala")
def consulta_sala(sala: str = Query(..., description="Nombre de la sala")):
    logger.info(f"consulta por sala recibida: {sala}")
    try:
        df_filtrado = cache.consulta_por_sala(sala)
        if df_filtrado.empty:
            logger.warning(f"No hay registros para sala '{sala}'")
            raise HTTPException(status_code=404, detail="no existen registros para esa sala.")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"consulta_sala_{sala}_{timestamp}.json"
        ruta_completa = os.path.join("jsons", nombre_archivo)
        df_filtrado.to_json(ruta_completa, orient="records", date_format="iso")
        logger.info(f"Consulta por sala '{sala}' guardada en {ruta_completa}")

        return {
            "mensaje": f"Consulta guardada en {ruta_completa}",
            "resultados": df_filtrado.to_dict(orient="records")
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en consulta por sala '{sala}': {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Error interno en el servidor.")


@app.post("/consulta-fecha")
def consulta_fecha(rango: FechaRango):
    logger.info(f"consulta por rango de fechas: desde {rango.desde} hasta {rango.hasta}")

    try:

        desde = rango.desde
        hasta = rango.hasta
        if desde.tzinfo is not None:
            desde = desde.replace(tzinfo=None)
        if hasta.tzinfo is not None:
            hasta = hasta.replace(tzinfo=None)

        logger.info(f"filtrando en caché entre {desde} y {hasta}")

        df_filtrado = cache.consulta_por_timestamp(desde, hasta)

        logger.info(f"cantidad de registros:  {len(df_filtrado)}")

        if df_filtrado.empty:
            logger.warning(f"no se encontraron registros entre el rango de {desde} y {hasta}")
            raise HTTPException(status_code=404, detail="no se encontraron registros en esa fecha.")

        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"consulta_rango_{timestamp_str}.json"
        ruta_completa = os.path.join("jsons", nombre_archivo)


        df_filtrado.to_json(ruta_completa, orient="records", date_format="iso")
        logger.info(f"consulta por fechas guardada en {ruta_completa}")

        return {
            "mensaje": f"Consulta exitosa desde {desde} hasta {hasta}",
            "resultados": df_filtrado.to_dict(orient="records")
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en consulta por rango de fecha: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="error servidor.")
