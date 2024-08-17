import math
import numpy as np

# 두 점 (point1, point2) 사이의 기울기를 계산하는 함수
def gradient(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    # x값이 동일한 경우, 즉 수직선의 경우 기울기가 무한대가 되므로 이를 처리
    if x2 - x1 == 0:
        return float('inf')  # 기울기가 무한대인 경우 반환
    
    return (y2 - y1) / (x2 - x1)

# 두 각도 a와 b의 차이를 계산하는 함수
def anglediff(a, b): 
    k = abs(a - b) % 180
    if abs(k - 180) < k:
        return k - 180
    else:
        return k

# 설계 정보
deltay = 19 / 2  # mm, LAG delta y
r0 = 40

r_AngleBlock = r0 + deltay

# 주축과 AngleBlock축 (편의상 이심축)의 기울기 관계
theta = 0  # AngleBlock 축에 대한 초기 각도

# 주축 기준 위치 계산
angleblock_theta = []  # 각도 (theta) 저장용 리스트
angleblock_x = []  # x 좌표 저장용 리스트
angleblock_y = []  # y 좌표 저장용 리스트
angleblock_ = []  # (theta, x, y) 튜플 저장용 리스트

# 주어진 각도 범위에서 각도를 변화시키며 x, y 좌표 계산
for theta in np.arange(start=0, stop=2 * math.pi, step=2 * math.pi / 1000):
    x = math.cos(theta) * r_AngleBlock
    y = math.sin(theta) * r_AngleBlock + deltay
    angleblock_theta.append(np.arctan2(x, y))
    angleblock_x.append(x)
    angleblock_y.append(y)
    angleblock_.append((theta, x, y))
# 여기까지 AngleBlock 변환 완료

# AngleBlock에서 발생하는 최대 각도 차이 계산
anglediff_ = []

for i in range(1000):
    previousdot = (angleblock_x[i-1], angleblock_y[i-1])  # 이전 점
    nextdot = (angleblock_x[(i+1) % len(angleblock_)], angleblock_y[(i+1) % len(angleblock_)])  # 다음 점
    nowdot = (angleblock_x[i], angleblock_y[i])  # 현재 점

    angleblock_gradient = gradient(previousdot, nextdot)  # AngleBlock의 기울기 계산

    angleblock_angle = math.degrees(np.arctan(angleblock_gradient))  # AngleBlock의 각도 계산
    CRA_angle = math.degrees(np.arctan(nowdot[1] / nowdot[0]))  # 현재 점에서 CRA 각도 계산

    anglediff_.append(anglediff(angleblock_angle, CRA_angle - 90))  # 각도 차이 계산 후 저장

# 여기까지가 Angle Difference 분석의 마지막 부분입니다.
