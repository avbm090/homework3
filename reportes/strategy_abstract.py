from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def generar(self, logs):
        pass
