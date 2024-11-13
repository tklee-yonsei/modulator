import unittest
from modulation.bpsk_modulator import BPSKModulator


class TestBPSKModulator(unittest.TestCase):
    def setUp(self):
        """BPSKModulator 인스턴스를 초기화."""
        self.modulator = BPSKModulator()

    def test_modulate_valid_bits(self):
        """유효한 비트 문자열을 변조했을 때 예상되는 심볼과 일치하는지 확인."""
        bits = "1100"
        expected_symbols = [-1, -1, 1, 1]
        self.assertEqual(self.modulator.modulate(bits), expected_symbols)

    def test_modulate_invalid_bit(self):
        """비트 문자열에 유효하지 않은 값이 포함될 때 ValueError가 발생하는지 확인."""
        with self.assertRaises(ValueError):
            self.modulator.modulate("1102")

    def test_demodulate_valid_symbols(self):
        """유효한 심볼을 복조했을 때 예상되는 비트 문자열과 일치하는지 확인."""
        symbols = [-1, -1, 1, 1]
        expected_bits = "1100"
        self.assertEqual(self.modulator.demodulate(symbols), expected_bits)

    def test_process_modulate_request_invalid_format(self):
        """변조 요청 처리 시 잘못된 형식이 들어올 때 ValueError가 발생하는지 확인."""
        with self.assertRaises(ValueError):
            self.modulator.process_modulate_request("1100a")

    def test_process_demodulate_request_invalid_format(self):
        """복조 요청 처리 시 잘못된 형식이 들어올 때 ValueError가 발생하는지 확인."""
        with self.assertRaises(ValueError):
            self.modulator.process_demodulate_request([[1, 1], [1, "a"]])


if __name__ == "__main__":
    unittest.main()
