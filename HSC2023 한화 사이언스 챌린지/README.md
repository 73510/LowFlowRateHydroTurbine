# LowFlowHydroTurbine
# 한화 사이언스 챌린지 프로젝트: 저유속 접이식 날개 수차

이 저장소는 한화 사이언스 챌린지에 출품한 저유속 접이식 날개 수차 프로젝트의 모든 자료를 포함하고 있습니다.

## 목차

1. [CFD 분석 데이터 (CFD Analysis Data)](#분석-데이터)
2. [아두이노 코드 (Arduino)](#아두이노-코드)
3. [CFD 최적화 (CFD Optimization)](#cfd-최적화)
4. [설계 파일 (Design Files)](#설계-파일)
5. [한화 사이언스 챌린지 제출 자료 (Files submitted to Hanwha Science Challenge)](#한화-사이언스-챌린지-제출-자료)

## [CFD 분석 데이터](./Analysis%20Data%20and%20Code/)

Computational Fluid Dynamics (CFD) 분석 및 최적화 관련 파일들이 이 섹션에 포함되어 있습니다.
[**Code and DXF**](./Analysis%20Data%20and%20Code/Code%20and%20DXF/)
- optimize_dxfV1
  - 수차의 CFD 결과 기반 토크 계산 및 최적화
  - 최적화 이후 Smoothing 코드
  - 분석 기반 DXF (Angleblock 단면 형상) 제작 코드
- full, half, straight, straightWF : 각 날개의 최적화 DXF 형상

## [아두이노 코드](./Arduino/)

실험 환경 제어 및 데이터 수집을 위한 아두이노 코드가 이 섹션에 있습니다.
- [어항 내 물의 흐름을 제어하는 코드 (단순 속도)](./Arduino/Motor_Control_SpeedControlOnly)
- [어항 내 물의 흐름을 제어하며 유속과 수차의 회전 속도를 IR 센서로 측정하는 코드](./Arduino/Motor_Control_SpeedControlandTachometer)

## CFD 최적화 코드
--자료 보충--

## [설계 파일](./설계/)

수차와 관련 부품들의 3D 모델링 파일 및 설계도면이 이 섹션에 있습니다.

- [STL](./설계/STL/) : 수차를 설계한 STL 파일을 모았습니다.
- [어항 설계](./설계/어항%20설계/) : 어항 구조물을 설치하는데 사용한 설계 파일입니다.
- Acryl Wall Arduino Placement : 아두이노를 설치하기 위해 만든 아크릴 판 구조물입니다.
- Acryl Wall : 아크릴 벽으로 어항 내부의 흐름을 나누어 순환하게 했습니다.

## [한화 사이언스 챌린지 제출 자료](./한화%20사이언스%20챌린지%20제출%20자료/)

프로젝트 관련 모든 문서 파일들이 이 섹션에 포함되어 있습니다:

- 아이디어 발표 자료
- 토론 발표 자료
- 한사챌 보고서
- 기존 연구 결과 자료
- 결과 전시물 계획서
- 판넬사진 출력 파일
- 기존 연구 특허출원번호 10-2010-0027024 수정 날개 접이식 수차 자료

이 문서들은 프로젝트의 전체적인 진행 과정, 연구 결과, 및 최종 제출 자료들을 포함하고 있습니다.