# GPIO counter8

[![데모 영상 썸네일](https://img.youtube.com/vi/-z-SnDnj8SU/0.jpg)](https://youtu.be/-z-SnDnj8SU)

이 스크립트는 `pinctrl` 명령어를 이용하여 시스템의 GPIO 핀을 제어하고, 3비트 이진 값을 주기적으로 출력합니다.

## 개요

스크립트는 숫자 0부터 7까지(총 8개)의 이진 표현을 GPIO 핀을 통해 출력하며, 각 숫자는 1초 간격으로 표시됩니다.

## 주요 기능

- GPIO 핀을 출력 모드로 초기화
- 3비트 이진 값(0~7)을 GPIO 핀을 통해 주기적으로 출력
- `CTRL+C` 또는 종료 시 신호를 감지하여 핀 상태를 초기화하고 안전하게 종료

## GPIO 핀

- GPIO 17
- GPIO 27
- GPIO 22

핀 배열은 **최하위 비트(LSB)**에서 **최상위 비트(MSB)** 순으로 정렬되어 있습니다.

## 스크립트 설명

### 초기화

```bash
pins=(17 27 22)

for p in "${pins[@]}"; do
    pinctrl set "$p" op
done
```

### 종료 처리

```bash
finish() {
    for p in "${pins[@]}"; do
        pinctrl set "$p" dl
    done
    exit
}

trap finish SIGINT SIGTERM
```

- 스크립트가 **CTRL+C** 또는 시스템 종료신호(SIGINT, SIGTERM)를 받을 경우, 각 GPIO 핀을 low로 설정한 후 종료합니다.

### 이진 출력 함수

```bash
output_bits() {
    val=$1
    for i in "${!pins[@]}"; do
        (( (val >> i) & 1 )) && pinctrl set "${pins[i]}" dh || pinctrl set "${pins[i]}" dl
    done
}
```

- 전달 받은 숫자를 이진수로 변환하여 각 비트에 해당하는 GPIO 핀을 high 또는 low로 설정합니다

### 메인 루프

```bash
while :; do
    for ((n=0; n<8; n++)); do
        output_bits "$n"
        sleep 1
    done
done
```

- 0부터 8까지의 값을 1초 간격으로 출력하며 무한반복합니다
- 각 숫자는 3비트 이진수로 GPIO 핀에 나타납니다.
