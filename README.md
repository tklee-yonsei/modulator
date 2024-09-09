# Team 2 - Coding API Documentation

This document provides an overview of the coding APIs developed by Team 2. The coding server handles encoding and decoding tasks using QAM and QPSK modulation techniques. 

## API Endpoints

### 1. QAM Encoding

- **URL**: `/encode/qam`
- **Method**: `POST`
- **Description**: Encodes a given signal using QAM (Quadrature Amplitude Modulation).

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "signal": [1, 0, 1, 1],
      "modulation_order": 16
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "encoded_signal": [
        {"I": 0.707, "Q": 0.707},
        {"I": -0.707, "Q": 0.707},
        {"I": -0.707, "Q": -0.707},
        {"I": 0.707, "Q": -0.707}
      ]
    }
    ```

### 2. QAM Decoding

- **URL**: `/decode/qam`
- **Method**: `POST`
- **Description**: Decodes a given encoded signal using QAM (Quadrature Amplitude Modulation).

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "encoded_signal": [
        {"I": 0.707, "Q": 0.707},
        {"I": -0.707, "Q": 0.707},
        {"I": -0.707, "Q": -0.707},
        {"I": 0.707, "Q": -0.707}
      ],
      "modulation_order": 16
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "decoded_signal": [1, 0, 1, 1]
    }
    ```

### 3. QPSK Encoding

- **URL**: `/encode/qpsk`
- **Method**: `POST`
- **Description**: Encodes a given signal using QPSK (Quadrature Phase Shift Keying).

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "signal": [1, 0, 1, 1],
      "modulation_order": 4
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "encoded_signal": [
        {"I": 1.0, "Q": 1.0},
        {"I": -1.0, "Q": 1.0},
        {"I": -1.0, "Q": -1.0},
        {"I": 1.0, "Q": -1.0}
      ]
    }
    ```

### 4. QPSK Decoding

- **URL**: `/decode/qpsk`
- **Method**: `POST`
- **Description**: Decodes a given encoded signal using QPSK (Quadrature Phase Shift Keying).

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "encoded_signal": [
        {"I": 1.0, "Q": 1.0},
        {"I": -1.0, "Q": 1.0},
        {"I": -1.0, "Q": -1.0},
        {"I": 1.0, "Q": -1.0}
      ],
      "modulation_order": 4
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "decoded_signal": [1, 0, 1, 1]
    }
    ```

## Getting Started

This section provides instructions on how to set up and run the preprocessing server in different environments.

### Local Development

To run the preprocessing server in a local development environment, ensure you have Docker installed and use the provided Dockerfile to build and run the server.

1. **Build the Docker image**:
    ```bash
    docker build -f Dockerfile.dev -t dev-coding-server .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 5002:5002 -v $(pwd):/app --rm --name container__dev-coding-server dev-coding-server
    ```

The server will be available on `http://localhost:5002`.

### mock

To run the preprocessing server in a mock environment, ensure you have Docker installed and use the provided Dockerfile to build and run the server.

1. **Build the Docker image**:
    ```bash
    docker build -f Dockerfile.mock -t mock-coding-server .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 6002:6002 --rm --name container__mock-coding-server mock-coding-server
    ```

The server will be available on `http://localhost:6002`.

## License

This project is licensed under the MIT License.
