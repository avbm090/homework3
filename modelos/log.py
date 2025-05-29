from datetime import datetime

class Log:

    def __init__(self, timestamp ,sala ,estado ,temperatura, humedad, co2, mensaje):
        self._timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        self._sala = str(sala)
        self._estado = str(estado)
        self._temperatura = float(temperatura)
        self._humedad = float(humedad)
        self._co2 = int(co2)
        self._mensaje = str(mensaje)

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def sala(self):
        return self._sala

    @property
    def estado(self):
        return self._estado

    @property
    def temperatura(self):
        return self._temperatura

    @property
    def humedad(self):
        return self._humedad

    @property
    def co2(self):
        return self._co2

    @property
    def mensaje(self):
        return self._mensaje
