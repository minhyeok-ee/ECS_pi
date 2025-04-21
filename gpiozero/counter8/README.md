# 🔢 3-Bit GPIO Binary Counter (counter8)

## 📹 동영상

[![썸네일](https://img.youtube.com/vi/yXRm9BlO1gY/hqdefault.jpg)](https://youtu.be/yXRm9BlO1gY)

---

## 📌 개요

이 프로젝트는 Raspberry Pi의 GPIO 핀을 활용한 3-bit 바이너리 카운터입니다.  
숫자 0부터 7까지 1초 간격으로 증가하며, 각 숫자의 이진수 표현을 3개의 LED로 시각화합니다.

---

## ⚙️ 하드웨어 구성

| 핀 번호 (BCM) | 연결된 장치 |
| ------------- | ----------- |
| 17            | LED (LSB)   |
| 27            | LED         |
| 22            | LED (MSB)   |

- 각 LED는 저항을 통해 GND에 연결되어야 합니다.
- Raspberry Pi의 GPIO 핀을 직접 제어하므로 `gpiozero` 라이브러리를 사용합니다.

---

## 🧠 코드 설명

코드는 총 4개의 주요 블록으로 구성되어 있으며, 각 블록은 다음과 같은 역할을 수행합니다:

---

### 🔹 1. 초기 설정 및 라이브러리 임포트

```python
from gpiozero import LED
from signal import signal, SIGINT, SIGTERM
from time import sleep
import sys
```

이 블록에서는 `gpiozero`, `signal`, `time`, `sys` 등의 필수 라이브러리를 불러옵니다.

- `gpiozero`는 Raspberry Pi의 GPIO 핀을 제어하는 라이브러리입니다.
- `signal`은 종료 시그널 처리에 사용되어, 프로그램이 안전하게 종료될 수 있도록 합니다.
- `time`은 시간 지연을 위한 `sleep()` 함수에 사용됩니다.
- `sys`는 프로그램 종료를 위해 사용됩니다.

---

### 🔹 2. 핀 번호와 출력 객체 초기화

```python
outputs = [LED(pin) for pin in PIN_NUMBERS]
```

- GPIO 핀 번호를 리스트로 정의하고, 각 핀에 연결된 LED 객체를 초기화합니다.
- `gpiozero` 라이브러리의 `LED` 클래스를 사용하여 각 핀을 제어할 수 있는 객체를 생성합니다.
- 이 객체는 프로그램 내에서 LED를 켜거나 끄는 동작을 수행할 수 있게 해줍니다.

---

### 🔹 3. 종료 시 LED OFF 처리 함수

```python
def shutdown_handler(sig, frame):
    print("\n[INFO] 종료 시그널 감지됨. 모든 핀 LOW 상태로 전환 중...")
    for out in outputs:
        out.off()
    sys.exit(0)

signal(SIGINT, shutdown_handler)
signal(SIGTERM, shutdown_handler)
```

프로그램이 종료되기 전, 모든 LED가 OFF 상태로 변환되도록 처리하는 함수입니다.  
종료 시그널(SIGINT, SIGTERM)을 감지하여 모든 LED를 끄고 안전하게 프로그램을 종료합니다.

- `signal(SIGINT, handle_exit)`와 `signal(SIGTERM, handle_exit)`는 종료 시그널이 들어오면 `handle_exit` 함수가 호출되도록 설정합니다.

---

### 🔹 4. 이진수 표시 함수

```python
def display_binary(num):
    for idx, out in enumerate(outputs):
        out.on() if (num >> idx) & 1 else out.off()
```

3-bit 카운터는 숫자 0부터 7까지의 값을 순차적으로 증가시키며, 이를 이진수로 표시합니다.  
`display_binary()` 함수는 숫자를 3비트 이진수로 변환하여 각 비트를 해당 LED에 반영합니다.

- `num >> idx`는 숫자 `num`을 오른쪽으로 `idx`만큼 비트 이동시킨 후, `& 1` 연산을 통해 해당 비트 값(0 또는 1)을 얻습니다.
- 예를 들어, 숫자 5를 이진수로 나타내면 `101`이 됩니다. 이때 첫 번째 LED는 1로 켜지고, 두 번째 LED는 0으로 꺼지며, 세 번째 LED는 1로 켜집니다.
- 이 과정을 통해 0부터 7까지의 숫자를 3개의 LED로 이진수 형태로 시각적으로 표현합니다.

---

### 🔹 5. 메인 카운터 루프

```python
def run_counter():
    print("[INFO] 3-bit 카운터 시작!")
    while True:
        for count in range(8):  # 0 ~ 7
            display_binary(count)
            sleep(1)
```

`run_counter()` 함수는 카운터의 핵심 동작을 수행합니다.

- `for count in range(8)`은 0부터 7까지의 값을 1초 간격으로 증가시키며 반복합니다.
- 각 카운트 값은 `display_binary(count)` 함수를 통해 해당하는 3-bit 이진수로 변환되어 LED에 출력됩니다.
- 예를 들어, `count` 값이 0일 때는 `000`으로 모든 LED가 꺼지고, `count` 값이 1일 때는 `001`로 첫 번째 LED만 켜집니다.
- 이 방식으로 0부터 7까지의 숫자가 순차적으로 LED에 표시됩니다.

---

### 🔹 6. 메인 진입점

```python
if __name__ == "__main__":
    try:
        run_counter()
    except KeyboardInterrupt:
        shutdown_handler(None, None)
```

- `if __name__ == "__main__":`로 시작하는 이 블록은 프로그램이 실행될 때 메인 카운터 루프를 시작합니다.
- 사용자가 `Ctrl + C`를 입력하면 `KeyboardInterrupt` 예외가 발생하고, 종료 시그널 처리 함수인 `handle_exit`가 호출되어 LED를 안전하게 끄고 프로그램을 종료합니다.

---

## ▶️ 실행 방법

```bash
python3 ~/bin/gpiozeros/counter8/counter8_gpiozeros.py
```

- 종료 시 Ctrl + C 를 누르면 LED가 안전하게 꺼지며 종료됩니다.

## 📄 파일 구조

counter8_gpiozeros.py
README.md
