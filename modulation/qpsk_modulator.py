from .interfaces import Modulator


class QPSKModulator(Modulator):
    def modulate(self, bits):
        if len(bits) % 2 != 0:
            raise ValueError("Bits length must be even for QPSK modulation")
        mapping = {"00": 1 + 1j, "01": -1 + 1j, "11": -1 - 1j, "10": 1 - 1j}
        symbols = []
        for i in range(0, len(bits), 2):
            bit_pair = bits[i : i + 2]
            if bit_pair in mapping:
                symbols.append(mapping[bit_pair])
            else:
                raise ValueError("Invalid bit sequence for QPSK modulation")
        return symbols

    def demodulate(self, symbols):
        demapping = {1 + 1j: "00", -1 + 1j: "01", -1 - 1j: "11", 1 - 1j: "10"}
        bits = ""
        for s in symbols:
            distances = {ref_symbol: abs(s - ref_symbol) for ref_symbol in demapping}
            closest_symbol = min(distances, key=distances.get)
            bits += demapping[closest_symbol]
        return bits

    def process_modulate_request(self, bits):
        if not isinstance(bits, str) or not all(b in "01" for b in bits):
            raise ValueError("Invalid bits format")
        symbols = self.modulate(bits)
        symbols_real_imag = [[s.real, s.imag] for s in symbols]
        return symbols_real_imag

    def process_demodulate_request(self, symbols_real_imag):
        try:
            symbols = [complex(s[0], s[1]) for s in symbols_real_imag]
        except (TypeError, IndexError, ValueError):
            raise ValueError("Invalid symbols data format")
        bits = self.demodulate(symbols)
        return bits
