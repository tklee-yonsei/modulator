from abc import ABC, abstractmethod

class CoderInterface(ABC):
    @abstractmethod
    def encode(self, signal, modulation_order):
        pass

    @abstractmethod
    def decode(self, encoded_signal, modulation_order):
        pass