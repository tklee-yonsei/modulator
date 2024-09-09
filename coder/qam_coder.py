from .interfaces import CoderInterface
import numpy as np

class QAMCoder(CoderInterface):
    def encode(self, signal, modulation_order):
        bits_per_symbol = int(np.log2(modulation_order))  # 각 심볼 당 필요한 비트 수
        m = int(np.sqrt(modulation_order))  # QAM 그리드의 차원

        # 입력 신호를 비트별로 매핑
        encoded_signal = []
        for bit in signal:
            if bit == 1:
                I, Q = 1.0 / np.sqrt(2), 1.0 / np.sqrt(2)
            else:
                I, Q = -1.0 / np.sqrt(2), -1.0 / np.sqrt(2)

            encoded_signal.append({"I": I, "Q": Q})

        return encoded_signal

    def decode(self, encoded_signal, modulation_order):
        bits_per_symbol = int(np.log2(modulation_order))  # 각 심볼 당 필요한 비트 수
        m = int(np.sqrt(modulation_order))  # QAM 그리드의 차원
        possible_symbols = self.generate_possible_symbols(modulation_order)

        decoded_signal = []
        for symbol in encoded_signal:
            I = symbol["I"]
            Q = symbol["Q"]

            # 수신된 (I, Q)와 가장 가까운 심볼을 찾기
            closest_symbol = min(possible_symbols, key=lambda s: np.linalg.norm([s["I"] - I, s["Q"] - Q]))

            # 가장 가까운 심볼의 비트 패턴을 복원하여 추가 (2비트씩)
            decoded_signal.extend(closest_symbol["bit"][:1])  # 필요한 비트 수만 추출

        return decoded_signal

    def generate_possible_symbols(self, modulation_order):
        bits_per_symbol = int(np.log2(modulation_order))  # 각 심볼 당 필요한 비트 수
        m = int(np.sqrt(modulation_order))  # QAM 그리드의 차원
        possible_symbols = []

        # 모든 가능한 QAM 심볼 생성
        for i in range(m):
            for q in range(m):
                I = (2 * i - (m - 1)) / (m - 1)
                Q = (2 * q - (m - 1)) / (m - 1)

                # I, Q에 해당하는 비트를 생성
                bit_pattern = format(i, f'0{bits_per_symbol // 2}b') + format(q, f'0{bits_per_symbol // 2}b')
                bit_list = list(map(int, bit_pattern))

                possible_symbols.append({"I": I, "Q": Q, "bit": bit_list})

        return possible_symbols