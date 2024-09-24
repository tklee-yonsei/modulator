from abc import ABC, abstractmethod


class Modulator(ABC):
    @abstractmethod
    def modulate(self, bits):
        pass

    @abstractmethod
    def demodulate(self, symbols):
        pass
