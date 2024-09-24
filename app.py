from flask import Flask, request, jsonify
from modulation.qpsk_modulator import QPSKModulator
from modulation.bpsk_modulator import BPSKModulator

app = Flask(__name__)

# 변조 방법 매핑 - 인스턴스를 미리 생성하여 재사용
modulators = {
    'qpsk': QPSKModulator(),
    'bpsk': BPSKModulator()
}

@app.route('/modulate/<method>', methods=['POST'])
def modulate(method):
    modulator = modulators.get(method)
    if modulator is None:
        return jsonify({'error_code': 1001, 'error': 'Invalid modulation method'}), 400

    bits = request.json.get('bits')
    if bits is None:
        return jsonify({'error_code': 1002, 'error': 'Missing bits data'}), 400

    try:
        symbols_real_imag = modulator.process_modulate_request(bits)
    except ValueError as e:
        return jsonify({'error_code': 1003, 'error': str(e)}), 400

    return jsonify({'symbols': symbols_real_imag})

@app.route('/demodulate/<method>', methods=['POST'])
def demodulate(method):
    modulator = modulators.get(method)
    if modulator is None:
        return jsonify({'error_code': 1001, 'error': 'Invalid demodulation method'}), 400

    symbols_real_imag = request.json.get('symbols')
    if symbols_real_imag is None:
        return jsonify({'error_code': 1004, 'error': 'Missing symbols data'}), 400

    try:
        bits = modulator.process_demodulate_request(symbols_real_imag)
    except ValueError as e:
        return jsonify({'error_code': 1005, 'error': str(e)}), 400

    return jsonify({'bits': bits})

if __name__ == '__main__':
    app.run(port=5002)
