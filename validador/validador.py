class LogValidador:

    @staticmethod
    def no_vacios(valor, campo):
        if valor is None or valor.strip() == '':
            raise ValueError(f"el valor de la columna '{campo}' no puede ser nulo ni estar vacío.")

    @staticmethod
    def validacion_logs(log):
        for campo, valor in vars(log).items():
            LogValidador.no_vacios(valor, campo)

