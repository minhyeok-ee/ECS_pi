# 🔆 순차 LED 점등 (domino4)

## 📹 동영상

[![썸네일](https://img.youtube.com/vi/5xsiYjXjxgA/hqdefault.jpg)](https://youtu.be/5xsiYjXjxgA)

---

## 📌 개요

이 프로젝트는 Raspberry Pi의 GPIO 핀을 활용하여 순차적으로 LED를 점등하는 프로그램입니다.  
각 LED는 1초 간격으로 점등되며, 전체 LED가 순차적으로 켜집니다. 종료 시, 모든 LED는 꺼집니다.

---

## ⚙️ 하드웨어 구성

| 핀 번호 (BCM) | 연결된 장치 |
| ------------- | ----------- |
| 17            | LED         |
| 27            | LED         |
| 22            | LED         |
| 10            | LED         |

- 각 LED는 저항을 통해 GND에 연결되어야 합니다.
- Raspberry Pi의 GPIO 핀을 직접 제어하므로 `gpiozero` 라이브러리를 사용합니다.

---

## 🧠 코드 설명

이 코드는 총 4개의 주요 블록으로 구성되어 있으며, 각 블록은 다음과 같은 역할을 수행합니다:

---

### 🔹 1. 초기 설정 및 라이브러리 임포트

```python
from gpiozero import LED
from time import sleep
from signal import signal, SIGINT, SIGTERM
import sys
```

- `gpiozero` 라이브러리: GPIO 핀 제어용으로, Raspberry Pi의 핀을 쉽게 제어할 수 있게 해줍니다.
- `time.sleep`: 1초 간격으로 LED를 순차적으로 점등하기 위한 시간 지연을 제공합니다.
- `signal`: 종료 시그널(SIGINT, SIGTERM)을 처리하기 위한 라이브러리로, 안전한 종료를 지원합니다.
- `sys`: 프로그램 종료를 위한 시스템 함수 호출을 가능하게 합니다.

---

### 🔹 2. 핀 번호와 출력 객체 초기화

```python
lights = [LED(pin) for pin in ACTIVE_PINS]
```

- 각 GPIO 핀 번호에 해당하는 LED 객체를 생성하여 이를 제어할 수 있도록 합니다.
- `ACTIVE_PINS` 리스트에 정의된 핀 번호에 맞는 LED 객체들을 생성하여 이후에 이들을 제어합니다.

---

### 🔹 3. 종료 시 LED OFF 처리 함수

```python
def handle_exit(sig, frame):
    print("\n[INFO] 종료 요청 수신됨. 모든 핀 OFF 처리 중...")
    for led in lights:
        led.off()
    sys.exit(0)

signal(SIGINT, handle_exit)
signal(SIGTERM, handle_exit)
```

프로그램이 종료되기 전, 모든 LED가 OFF 상태로 변환되도록 처리하는 함수입니다.  
종료 시그널(SIGINT, SIGTERM)을 감지하여 모든 LED를 끄고 안전하게 프로그램을 종료합니다.

- `signal(SIGINT, handle_exit)`와 `signal(SIGTERM, handle_exit)`는 종료 시그널이 들어오면 `handle_exit` 함수가 호출되도록 설정합니다.

---

### 🔹 4. 순차적으로 LED 점등 함수

```pyhon
def activate_only(index):
    for i, led in enumerate(lights):
        led.on() if i == index else led.off()
```

`activate_only(index)` 함수는 인덱스를 통해 특정 LED만 켜고 나머지 LED는 끄는 역할을 합니다.  
이 함수는 순차적으로 각 LED를 점등하는 방식으로, 각 LED는 1초 간격으로 켜집니다.  
`start_light_cycle()` 함수에서 이 기능을 반복문을 통해 실행하며, 순차적으로 각 LED를 켜고, 1초마다 상태를 변경합니다.

- 예: 첫 번째 LED가 켜지고, 1초 후 두 번째 LED가 켜지는 식으로 순차적으로 점등됩니다.

---

### 🔹 5. 메인 루프 함수

```python
def start_light_cycle():
    print("[INFO] 순차 LED 점등 시작.")
    total = len(lights)
    while True:
        for current in range(total):
            activate_only(current)
            sleep(1)
```

메인 루프는 `start_light_cycle()` 함수에서 시작되며, 프로그램이 계속해서 순차적으로 LED를 점등하는 작업을 수행합니다.

- `for current in range(total)`을 사용하여 각 LED를 순차적으로 점등하고, `sleep(1)`로 1초 간격을 두어 점등을 진행합니다.
- 이 루프는 프로그램이 종료될 때까지 반복되며, LED 점등을 반복적으로 실행합니다.

---

### 🔹 6. 메인 진입점

```python
if __name__ == "__main__":
    try:
        start_light_cycle()
    except KeyboardInterrupt:
        handle_exit(None, None)

```

- `if __name__ == "__main__":`로 시작하는 이 블록은 프로그램이 실행될 때 메인 카운터 루프를 시작합니다.
- 사용자가 `Ctrl + C`를 입력하면 `KeyboardInterrupt` 예외가 발생하고, 종료 시그널 처리 함수인 `handle_exit`가 호출되어 LED를 안전하게 끄고 프로그램을 종료합니다.

---

## ▶️ 실행 방법

```bash
python3 ~/bin/gpiozeros/sequential_led/sequential_led_gpiozeros.py
```

- 종료 시 Ctrl + C 를 누르면 LED가 안전하게 꺼지며 종료됩니다.

## 📄 파일 구조

domino4_gpiozeros.py
README.md # 프로젝트
