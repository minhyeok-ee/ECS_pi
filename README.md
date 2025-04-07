# Week5: GPIO 제어 스크립트 프로젝트

이 프로젝트는 Raspberry Pi와 같은 리눅스 기반 시스템에서 `pinctrl` 명령어를 사용해 GPIO 핀을 제어하는 Bash 스크립트 예제들을 포함하고 있습니다.  
2가지 예제(`counter8`, `domino4`)를 통해 기본적인 GPIO 출력, 이진수 표현, 순차 점등 제어를 익힐 수 있습니다.

## 🛠️ pinctrl & GPIO 간단 설명

- **GPIO (General Purpose Input/Output)**  
  GPIO는 범용 입출력 핀으로, 사용자가 직접 프로그래밍하여 전기 신호를 제어할 수 있습니다. LED 점등, 버튼 입력 등 다양한 하드웨어와 연결됩니다.

- **pinctrl**  
  `pinctrl`은 GPIO 핀의 동작을 제어하는 명령어 인터페이스입니다.  
  이 프로젝트에서는 `pinctrl set <핀 번호> op/dh/dl` 형식으로 핀의 동작을 설정합니다.
  - `op`: output 모드
  - `dh`: digital high (1)
  - `dl`: digital low (0)

## 📁 프로젝트 구조

```
week5/
├── counter8/
│ ├── counter8_source
│ └── README.md
├── domino4/
│ ├── domino4_source
│ └── README.md
└── README.md
```

## 📌 예제 설명

### ✅ counter8

- **기능**: 3개의 GPIO 핀을 사용하여 숫자 0부터 7까지 이진수로 출력
- **활용**: LED를 이용한 이진 카운터 시각화
- **사용 핀**: GPIO 17, 27, 22

### ✅ domino4

- **기능**: 여러 개의 핀 중 하나씩 순차적으로 점등
- **활용**: 도미노 효과, 시퀀스 표시, LED 런닝 라이트
- **사용 핀**: GPIO 17, 27, 22, 10

## 🚀 실행 방법

각 폴더 내부에서 아래 명령어로 실행할 수 있습니다.

```bash
chmod +x script.sh
./script.sh
```

**pinctrl**이 설치되어 있어야 하며, GPIO 접근을 위해 **sudo** 권한이 필요할 수 있습니다.
