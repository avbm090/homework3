from .estrategia import EstadoSala
from .estrategia import AlertasCriticas
from logs.log_config import logger

class ReporteFactory:
    @staticmethod
    def crear_reporte(tipo):
        if tipo == "estado_sala":
            logger.info("creando el reporte: estado por sala")
            return EstadoSala()
        elif tipo == "alertas_criticas":
            logger.info("creando el reporte: alertas críticas")
            return AlertasCriticas()
        else:
            logger.error(f"Tipo de reporte no identificado: {tipo}")
            raise ValueError(f"Tipo de reporte no identificado: {tipo}")
