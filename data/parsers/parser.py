from modelos.log import Log
import pandas as pd

class LogParser:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df_logs = None

    def parse_csv_a_logs(self):
        logs = []
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            next(f)  
            for linea in f:
                if not linea.strip():
                    continue
                partes = linea.strip().split(',', 6)  # 7 col
                if len(partes) < 7:
                    continue
                log_obj = Log(*partes)
                logs.append(log_obj)

        df = pd.DataFrame([{
            'timestamp': log.timestamp,
            'sala': log.sala,
            'estado': log.estado,
            'temperatura': log.temperatura,
            'humedad': log.humedad,
            'co2': log.co2,
            'mensaje': log.mensaje
        } for log in logs])

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        self.df_logs = df
        return df

    def to_json(self):
        if self.df_logs is None:
            self.parse_csv_a_logs()
        return self.df_logs.to_json(orient='records', date_format='iso')
