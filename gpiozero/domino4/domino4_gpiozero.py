#!/usr/bin/env python3

from gpiozero import LED
from time import sleep
from signal import signal, SIGINT, SIGTERM
import sys

# 사용할 GPIO 핀 번호 (BCM 기준)
ACTIVE_PINS = [17, 27, 22, 10]

# LED 객체 초기화
lights = [LED(pin) for pin in ACTIVE_PINS]

# 종료 시 전체 LED OFF 처리
def handle_exit(sig, frame):
    print("\n[INFO] 종료 요청 수신됨. 모든 핀 OFF 처리 중...")
    for led in lights:
        led.off()
    sys.exit(0)

# 시그널 핸들링 등록
signal(SIGINT, handle_exit)
signal(SIGTERM, handle_exit)

# 특정 인덱스만 켜고 나머지는 끄는 함수
def activate_only(index):
    for i, led in enumerate(lights):
        led.on() if i == index else led.off()

# 메인 루프 함수
def start_light_cycle():
    print("[INFO] 순차 LED 점등 시작.")
    total = len(lights)
    while True:
        for current in range(total):
            activate_only(current)
            sleep(1)

# 실행부
if __name__ == "__main__":
    try:
        start_light_cycle()
    except KeyboardInterrupt:
        handle_exit(None, None)
