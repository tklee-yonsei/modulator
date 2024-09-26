from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/modulate/<method>', methods=['POST'])
def modulate(method):
    bits = request.json.get('bits')
    # Mock: 각 비트를 [비트값, 0] 형태로 변환
    symbols = [[int(bit), 0] for bit in bits]
    return jsonify({'symbols': symbols})

@app.route('/demodulate/<method>', methods=['POST'])
def demodulate(method):
    symbols = request.json.get('symbols')
    # Mock: 실수부의 값이 0 이상이면 '0', 그렇지 않으면 '1'
    bits = ''.join(['0' if s[0] >= 0 else '1' for s in symbols])
    return jsonify({'bits': bits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6002)  # 모든 인터페이스에서 수신하도록 설정
