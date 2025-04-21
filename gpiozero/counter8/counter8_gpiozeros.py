#!/usr/bin/env python3

from gpiozero import LED
from signal import signal, SIGINT, SIGTERM
from time import sleep
import sys

# 사용할 GPIO 핀 목록 (BCM 번호)
PIN_NUMBERS = [17,27,22]

# 각 핀에 해당하는 LED 객체 생성
outputs = [LED(pin) for pin in PIN_NUMBERS]

# 종료 시 호출되는 정리 함수
def shutdown_handler(sig, frame):
    print("\n[INFO] 종료 시그널 감지됨. 모든 핀 LOW 상태로 전환 중...")
    for out in outputs:
        out.off()
    sys.exit(0)

# 시그널 등록
signal(SIGINT, shutdown_handler)
signal(SIGTERM, shutdown_handler)

# 숫자를 이진수로 변환하여 핀 상태로 반영
def display_binary(num):
    for idx, out in enumerate(outputs):
        out.on() if (num >> idx) & 1 else out.off()

# 메인 실행부
def run_counter():
    print("[INFO] 3-bit 카운터 시작!")
    while True:
        for count in range(8):  # 0 ~ 7
            display_binary(count)
            sleep(1)

# 실행 시작
if __name__ == "__main__":
    try:
        run_counter()
    except KeyboardInterrupt:
        shutdown_handler(None, None)