# GPIO domino4

[![데모 영상 썸네일](https://img.youtube.com/vi/1ECSAs7Bj0w/0.jpg)](https://youtu.be/1ECSAs7Bj0w)

이 스크립트는 `pinctrl` 명령어를 사용하여 GPIO 핀들을 제어하고, 지정된 핀들을 순차적으로 1초 간격으로 점등하는 방식으로 작동합니다.

## 개요

스크립트는 총 4개의 GPIO 핀을 설정하고, 하나씩 순서대로 High로 설정하여 불이 하나씩 돌아가듯이 점등되게 만듭니다.

## 주요 기능

- 지정된 GPIO 핀 4개를 출력 모드로 초기화
- 배열 인덱스를 기준으로 하나씩만 High(dh)로 설정하며 순차 점등
- 무한 반복하며 1초 간격으로 점등 순서를 변경

## 사용되는 GPIO 핀

- GPIO 17
- GPIO 27
- GPIO 22
- GPIO 10

순서대로 하나씩 점등됩니다.

## 스크립트 설명

### 핀 초기화

```bash
pins=(17 27 22 10)

for pin in "${pins[@]}"; do
    pinctrl set "$pin" op
done
```

- 각 GPIO 핀을 출력 모드로 설정합니다.

### LED 하나만 점등하는 함수

```bash
light_one() {
    local on_idx=$1
    for idx in "${!pins[@]}"; do
        if [[ "$idx" -eq "$on_idx" ]]; then
            pinctrl set "${pins[$idx]}" dh
        else
            pinctrl set "${pins[$idx]}" dl
        fi
    done
}
```

- 입력된 인덱스에 해당하는 핀만 high로 설정하고 나머지는 모두 low로 설정합니다.

### 메인 루프

```bash
while :; do
    for ((i = 0; i < ${#pins[@]}; i++)); do
        light_one "$i"
        sleep 1
    done
done
```

- 핀 배열의 길이만큼 순차적으로 인덱스를 증가시키며 **light_one**을 호출합니다.
- 각 핀은 1초 동안 점등되고 다음 핀으로 넘어가면서 반복됩니다.
