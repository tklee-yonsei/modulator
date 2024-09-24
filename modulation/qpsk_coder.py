from .interfaces import CoderInterface
import numpy as np

class QPSKCoder(CoderInterface):
    def encode(self, signal, modulation_order):
        if modulation_order != 4:
            raise ValueError("QPSK는 modulation_order가 4여야 합니다.")
        
        # QPSK에서는 심볼 당 2비트 사용
        bits_per_symbol = int(np.log2(modulation_order))
        encoded_signal = []

        # 2비트씩 나눠 QPSK 인코딩 수행
        for i in range(0, len(signal), bits_per_symbol):
            # 비트 쌍을 가져옵니다.
            bit_pair = signal[i:i + bits_per_symbol]

            if len(bit_pair) < bits_per_symbol:
                # 남은 비트가 부족한 경우 0으로 패딩
                bit_pair += [0] * (bits_per_symbol - len(bit_pair))

            # 비트 쌍을 I와 Q 값으로 매핑
            if bit_pair == [0, 0]:
                I, Q = 1 / np.sqrt(2), 1 / np.sqrt(2)  # 45도 (π/4)
            elif bit_pair == [0, 1]:
                I, Q = -1 / np.sqrt(2), 1 / np.sqrt(2)  # 135도 (3π/4)
            elif bit_pair == [1, 1]:
                I, Q = -1 / np.sqrt(2), -1 / np.sqrt(2)  # 225도 (5π/4)
            elif bit_pair == [1, 0]:
                I, Q = 1 / np.sqrt(2), -1 / np.sqrt(2)  # 315도 (7π/4)

            encoded_signal.append({"I": I, "Q": Q})

        return encoded_signal

    def decode(self, encoded_signal, modulation_order):
        if modulation_order != 4:
            raise ValueError("QPSK는 modulation_order가 4여야 합니다.")

        # QPSK에서는 심볼 당 2비트 사용
        bits_per_symbol = int(np.log2(modulation_order))
        decoded_signal = []

        # 가능한 심볼의 I와 Q 값을 정의합니다.
        symbol_map = {
            (1 / np.sqrt(2), 1 / np.sqrt(2)): [0, 0],   # 45도 (π/4)
            (-1 / np.sqrt(2), 1 / np.sqrt(2)): [0, 1],  # 135도 (3π/4)
            (-1 / np.sqrt(2), -1 / np.sqrt(2)): [1, 1], # 225도 (5π/4)
            (1 / np.sqrt(2), -1 / np.sqrt(2)): [1, 0]   # 315도 (7π/4)
        }

        # 각 수신된 심볼에 대해 디코딩 수행
        for symbol in encoded_signal:
            I, Q = symbol["I"], symbol["Q"]

            # 가능한 심볼과 가장 가까운 (I, Q) 값을 찾습니다.
            closest_symbol = min(symbol_map.keys(), key=lambda s: np.linalg.norm([s[0] - I, s[1] - Q]))

            # 대응되는 비트 패턴을 디코딩 결과에 추가합니다.
            decoded_signal.extend(symbol_map[closest_symbol])

        return decoded_signal