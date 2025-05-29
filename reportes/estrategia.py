from .strategy_abstract import Strategy
from logs.log_config import logger

class EstadoSala(Strategy):

    def generar(self, df_logs, sala):
        try:
            if 'sala' not in df_logs.columns or 'estado' not in df_logs:
                raise ValueError('no se encuentra el campo sala o estado')
            
            df_sala=df_logs[df_logs['sala']==sala]

            if df_sala.empty:
                logger.warning(f"no se encontraron registros para el tipo'{sala}'.")
                print(f"no se encontraron registros para el tipo'{sala}'.")
                return
        
            resultado = df_sala['estado'].value_counts().to_dict()

            for estado, cantidad in resultado.items():
                logger.info(f"sala '{sala}': estado '{estado} con {cantidad} logs '")
                print(f"cantidad de logs con {estado}: {cantidad}")


        except Exception as a:
            logger.error(f"Error generando reporte EstadoSala: {a}")
            print(f"no se pudo generar el reporte: {a}")

class AlertasCriticas(Strategy):

    def generar(self, df_logs, estado):
        try:
            if 'estado' not in df_logs.columns:
                raise ValueError('no se encontró el campo estado')
            
            df_warnings = df_logs['estado'].value_counts().get('WARNING', 0)
        
            #df_warnings = df_logs[df_logs['estado']=='WARNING']
            logger.info(f"cantidad de alertas críticas: {df_warnings}")
            print(f"cantidad de alertas críticas: {df_warnings}")

        except Exception as a:
            logger.error(f"no se pudo generar el reporte: {a}")
            print(f"no se pudo generar el reporte: {a}")