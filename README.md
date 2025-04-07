# GPIO 제어 스크립트

이 프로젝트는 Raspberry Pi에서 `pinctrl` 명령어를 사용해 GPIO 핀을 제어하는 2가지 예제(`counter8`, `domino4`)를 통한
기본적인 GPIO 출력, 이진수 표현, 순차 점등 제어 연습에 대한 내용입니다.

## 🛠️ pinctrl & GPIO 간단 설명

- **GPIO (General Purpose Input/Output)**  
  GPIO는 Raspberry Pi에서 I/O 핀을 확장해 사용하는 것으로 LED 점등, 버튼 입력 등 다양한 하드웨어와 연결됩니다.

- **pinctrl**  
  `pinctrl`은 GPIO 핀의 동작을 제어하는 명령어 인터페이스입니다.  
  이 프로젝트에서는 `pinctrl set <핀 번호> op/dh/dl` 형식으로 핀의 동작을 설정합니다.
  - `op`: output 모드
  - `dh`: digital high (1)
  - `dl`: digital low (0)

## 📌 예제 설명

### ✅ counter8

- **기능**: 3개의 GPIO 핀을 사용하여 숫자 0부터 7까지 이진수로 출력
- **활용**: LED를 이용한 이진 카운터 시각화
- **사용 핀**: GPIO 17, 27, 22

### ✅ domino4

- **기능**: 여러 개의 핀 중 하나씩 순차적으로 점등
- **활용**: 도미노 효과, 시퀀스 표시, LED 런닝 라이트
- **사용 핀**: GPIO 17, 27, 22, 10

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

ssh 연결이 불안정한지 촬영중에 계속 끊어져서 일단 connect.raspberry.com에서 화면공유하여 프로젝트 진행하였습니다.
소스코드와 readme 파일은 별도의 파일을 만들어서 github 업로드 용으로 사용하였습니다.
