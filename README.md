# 팀 2 - 변복조 API 문서

변복조 서버를 위한 API 문서입니다.

## API 엔드포인트

### 1. 변조

- **URL**: `/modulate/<method>`
- **Parameters**: 
  - `<method>`: `qpsk`, `bpsk`
- **Method**: `POST`
- **Description**: 신호를 변조 후, 변조된 신호를 돌려줍니다.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "bits": "11010011"
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "symbols": [[real1, imag1], [real2, imag2], ...]
    }
    ```

### 2. 복조

- **URL**: `/decode/<method>`
- **Parameters**: 
  - `<method>`: `qpsk`, `bpsk`
- **Method**: `POST`
- **Description**: 신호를 복조 후, 복조된 신호를 돌려줍니다.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "symbols": [[real1, imag1], [real2, imag2], ...]
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "bits": "11010011"
    }
    ```

## 에러

- **2001**: Invalid encoding/decoding method
- **2002**: Missing data_bits/coded_bits
- **2003**: Invalid data_bits/coded_bits format

## 시작하기

이 섹션에서는 다양한 환경에서 전처리 서버를 설정하고, 
실행하는 방법에 대한 지침을 제공합니다.

### 로컬 개발

로컬 개발 환경에서 전처리 서버를 실행하려면, 
Docker가 설치되어 있는지 확인하고, 
제공된 Dockerfile을 사용하여 서버를 빌드하고 실행하세요.

1. **Docker 이미지 빌드**:
    ```bash
    docker build -f Dockerfile.dev -t dev-coding-server .
    ```

2. **Docker 컨테이너 실행**:
    ```bash
    docker run -p 5002:5002 -v $(pwd):/app --rm --name container__dev-coding-server dev-coding-server
    ```

서버는 `http://localhost:5002`에서 사용할 수 있습니다.

### mock

mock 환경에서 전처리 서버를 실행하려면, 
Docker가 설치되어 있는지 확인하고, 
제공된 Dockerfile을 사용하여 서버를 빌드하고 실행하세요.

1. **Docker 이미지 빌드**:
    ```bash
    docker build -f Dockerfile.mock -t mock-coding-server .
    ```

2. **Docker 컨테이너 실행**:
    ```bash
    docker run -p 6002:6002 --rm --name container__mock-coding-server mock-coding-server
    ```

서버는 `http://localhost:6002`에서 사용할 수 있습니다.

## License

This project is licensed under the MIT License.
