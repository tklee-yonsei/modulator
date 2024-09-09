from flask import Flask, jsonify, request
from coder.qam_coder import QAMCoder
from coder.qpsk_coder import QPSKCoder

app = Flask(__name__)

# QAM 및 QPSK 인코더/디코더 인스턴스 생성
qam_coder = QAMCoder()
qpsk_coder = QPSKCoder()

# QAM Encoding endpoint
@app.route("/encode/qam", methods=["POST"])
def encode_qam():
    input_data = request.json
    signal = input_data.get("signal", [])
    modulation_order = input_data.get("modulation_order", 16)

    # QAM 인코딩 처리
    encoded_signal = qam_coder.encode(signal, modulation_order)
    
    response_data = {"encoded_signal": encoded_signal}
    return jsonify(response_data)

# QAM Decoding endpoint
@app.route("/decode/qam", methods=["POST"])
def decode_qam():
    input_data = request.json
    encoded_signal = input_data.get("encoded_signal", [])
    modulation_order = input_data.get("modulation_order", 16)

    # QAM 디코딩 처리
    decoded_signal = qam_coder.decode(encoded_signal, modulation_order)
    
    response_data = {"decoded_signal": decoded_signal}
    return jsonify(response_data)

# QPSK Encoding endpoint
@app.route("/encode/qpsk", methods=["POST"])
def encode_qpsk():
    input_data = request.json
    signal = input_data.get("signal", [])
    modulation_order = input_data.get("modulation_order", 4)

    # QPSK 인코딩 처리
    encoded_signal = qpsk_coder.encode(signal, modulation_order)
    
    response_data = {"encoded_signal": encoded_signal}
    return jsonify(response_data)

# QPSK Decoding endpoint
@app.route("/decode/qpsk", methods=["POST"])
def decode_qpsk():
    input_data = request.json
    encoded_signal = input_data.get("encoded_signal", [])
    modulation_order = input_data.get("modulation_order", 4)

    # QPSK 디코딩 처리
    decoded_signal = qpsk_coder.decode(encoded_signal, modulation_order)
    
    response_data = {"decoded_signal": decoded_signal}
    return jsonify(response_data)

if __name__ == "__main__":
    # Flask 서버 실행
    app.run(host="0.0.0.0", port=5002)