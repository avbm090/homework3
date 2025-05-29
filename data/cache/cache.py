from datetime import datetime, timedelta
import pandas as pd


class Cache:
    def __init__(self, df_logs, ventana_min=5):
        self.ventana = timedelta(minutes=ventana_min)
        self.df_logs = df_logs.copy()
        self.ultima_actualizacion = datetime.now()

    def actualizar(self, nuevo_df):
        ahora = datetime.now()
        limite_inferior = ahora - self.ventana

        nuevo_df['timestamp'] = pd.to_datetime(nuevo_df['timestamp'])

        # se filtra lo que caiga mayor al valor inferior de la ventana
        dentro_de_ventana = nuevo_df[nuevo_df['timestamp'] >= limite_inferior]

        self.df_logs = pd.concat([self.df_logs, dentro_de_ventana], ignore_index=True)
        self.ultima_actualizacion = ahora
        self.limpiar_logs_antiguos()


    def limpiar_logs_antiguos(self):
        limite_inferior = datetime.now() - self.ventana
        self.df_logs['timestamp'] = pd.to_datetime(self.df_logs['timestamp'])
        self.df_logs = self.df_logs[self.df_logs['timestamp'] >= limite_inferior]

    def consulta_por_sala(self, sala):
        return self.df_logs[self.df_logs['sala'] == sala]

    def consulta_por_timestamp(self, desde, hasta):
        entre = (self.df_logs['timestamp'] >= desde) & (self.df_logs['timestamp'] <= hasta)
        return self.df_logs[entre]
