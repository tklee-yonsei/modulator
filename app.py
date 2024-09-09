from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock QAM Encoding endpoint
@app.route("/encode/qam", methods=["POST"])
def mock_encode_qam():
    input_data = request.json
    signal_length = len(input_data.get("signal", []))
    
    # 임의의 encoded_signal 생성 (길이 맞춤)
    encoded_signal = [{"I": 0.707, "Q": 0.707} for _ in range(signal_length)]
    
    response_data = {"encoded_signal": encoded_signal}
    return jsonify(response_data)

# Mock QAM Decoding endpoint
@app.route("/decode/qam", methods=["POST"])
def mock_decode_qam():
    input_data = request.json
    encoded_signal = input_data.get("encoded_signal", [])
    
    # 입력 신호의 길이와 동일한 길이의 decoded_signal 생성
    decoded_signal = [1] * len(encoded_signal)
    
    response_data = {"decoded_signal": decoded_signal}
    return jsonify(response_data)

# Mock QPSK Encoding endpoint
@app.route("/encode/qpsk", methods=["POST"])
def mock_encode_qpsk():
    input_data = request.json
    signal_length = len(input_data.get("signal", []))
    
    # 임의의 encoded_signal 생성 (길이 맞춤)
    encoded_signal = [{"I": 1.0, "Q": 1.0} for _ in range(signal_length)]
    
    response_data = {"encoded_signal": encoded_signal}
    return jsonify(response_data)

# Mock QPSK Decoding endpoint
@app.route("/decode/qpsk", methods=["POST"])
def mock_decode_qpsk():
    input_data = request.json
    encoded_signal = input_data.get("encoded_signal", [])
    
    # 입력 신호의 길이와 동일한 길이의 decoded_signal 생성
    decoded_signal = [1] * len(encoded_signal)
    
    response_data = {"decoded_signal": decoded_signal}
    return jsonify(response_data)

if __name__ == "__main__":
    # Flask 서버 실행
    app.run(host="0.0.0.0", port=5002)