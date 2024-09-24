from .interfaces import Modulator


class BPSKModulator(Modulator):
    def modulate(self, bits):
        mapping = {"0": 1, "1": -1}
        symbols = []
        for bit in bits:
            if bit in mapping:
                symbols.append(mapping[bit])
            else:
                raise ValueError("Invalid bit for BPSK modulation")
        return symbols

    def demodulate(self, symbols):
        bits = ""
        for s in symbols:
            bit = "0" if s.real >= 0 else "1"
            bits += bit
        return bits

    def process_modulate_request(self, bits):
        if not isinstance(bits, str) or not all(b in "01" for b in bits):
            raise ValueError("Invalid bits format")
        symbols = self.modulate(bits)
        symbols_real_imag = [[s.real, 0] for s in symbols]
        return symbols_real_imag

    def process_demodulate_request(self, symbols_real_imag):
        try:
            symbols = [complex(s[0], s[1]) for s in symbols_real_imag]
        except (TypeError, IndexError, ValueError):
            raise ValueError("Invalid symbols data format")
        bits = self.demodulate(symbols)
        return bits
