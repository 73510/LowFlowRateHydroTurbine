import numpy as np
import ezdxf
import math
import matplotlib.pyplot as plt

from ezdxf import recover
from ezdxf.addons.drawing import matplotlib
import numpy as np


# 두 점 (point1, point2) 사이의 기울기를 계산하는 함수
def gradient(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    # x 값이 동일한 경우, 즉 수직선의 경우 기울기가 무한대가 되므로 이를 처리
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

# 반지름과 각도 리스트를 받아서 x, y 좌표 리스트로 변환하는 함수
def rthetatoxy(l_): 
    x_ = []
    y_ = []
    for elements in l_:
        x_.append(elements[0] * math.cos(elements[1]))
        y_.append(elements[0] * math.sin(elements[1]))

    return x_, y_

# 주어진 점 (x, y)를 특정 각도(angle)만큼 회전시키는 함수
def rotate_point(x, y, angle):
    x_new = x * np.cos(angle) - y * np.sin(angle)
    y_new = x * np.sin(angle) + y * np.cos(angle)
    return x_new, y_new

# 사각형의 중심 좌표, 너비, 높이, 회전 각도를 받아 사각형의 네 꼭지점 좌표를 반환하는 함수
def get_corners(rectangle):
    cx, cy, w, h, angle = rectangle
    half_w, half_h = w / 2, h / 2
    corners = [
        (-half_w, -half_h),
        (half_w, -half_h),
        (half_w, half_h),
        (-half_w, half_h)
    ]
    rotated_corners = [rotate_point(x, y, angle) for x, y in corners]
    translated_corners = [(x + cx, y + cy) for x, y in rotated_corners]
    return np.array(translated_corners)

# 다각형(polygon)을 주어진 축(axis)에 투영하고, 투영된 점들의 범위를 반환하는 함수
def project_polygon(axis, polygon):
    dots = np.dot(axis, polygon.T)
    return [np.min(dots), np.max(dots)]

# 두 투영된 범위가 겹치는지 여부를 확인하는 함수
def axis_overlap(a_min, a_max, b_min, b_max):
    return a_min <= b_max and b_min <= a_max

# 두 사각형이 교차하는지 여부를 판단하는 함수
def rectangles_intersect(rect1, rect2):
    corners1 = get_corners(rect1)
    corners2 = get_corners(rect2)
    
    # 두 사각형의 가장자리와 수직인 축(axes) 벡터를 구함
    axes1 = corners1 - np.roll(corners1, 1, axis=0)
    axes2 = corners2 - np.roll(corners2, 1, axis=0)
    axes = np.vstack([axes1, axes2])
    
    axes = axes / np.linalg.norm(axes, axis=1)[:, None]  # 축을 정규화
    
    # 각 축에 대해 사각형이 겹치는지 확인
    for axis in axes:
        p1 = project_polygon(axis, corners1)
        p2 = project_polygon(axis, corners2)
        
        if not axis_overlap(p1[0], p1[1], p2[0], p2[1]):
            return False  # 어떤 축에서라도 투영이 겹치지 않으면 교차하지 않음
    
    return True

# 점 B에서 점 A를 빼는 함수 (선분 AB의 벡터를 반환)
def coord_minus(A, B):
    return [B[0] - A[0], B[1] - A[1]]

# 점 A와 점 B를 더하는 함수
def coord_plus(A, B): 
    return [B[0] + A[0], B[1] + A[1]]

# 점 A를 상수 k로 곱하는 함수
def coord_multiply(A, k): 
    return [k * A[0], k * A[1]]

# 점 P와 선분 AB 사이의 최소 거리를 계산하는 함수
def distance_between_point_and_segment(P, A, B):
    AP = coord_minus(A, P)
    AB = coord_minus(A, B)
    t = np.dot(AP, AB) / np.dot(AB, AB)
    if 0 <= t <= 1:
        C = coord_plus(A, coord_multiply(AB, t))
        return np.linalg.norm(coord_minus(C, P))
    else:
        return min(np.linalg.norm(coord_minus(A, P)), np.linalg.norm(coord_minus(B, P)))

# 두 사각형 사이의 최소 거리를 계산하는 함수
def min_distance_between_rectangles(rect1, rect2):

    if rectangles_intersect(rect1, rect2):
        return 0  # 두 사각형이 교차하는 경우 거리 0 반환
    
    corners1 = get_corners(rect1)
    corners2 = get_corners(rect2)
    
    min_distance1 = float('inf')
    
    for P in corners1:
        for i in range(len(corners2)):
            A, B = corners2[i], corners2[(i + 1) % len(corners2)]
            dist = distance_between_point_and_segment(P, A, B)
            min_distance1 = min(min_distance1, dist)
            
    min_distance2 = float('inf')
    
    for P in corners2:
        for i in range(len(corners1)):
            A, B = corners1[i], corners1[(i + 1) % len(corners1)]
            dist = distance_between_point_and_segment(P, A, B)
            min_distance2 = min(min_distance2, dist)

    return min(min_distance2, min_distance1)

# 두 점 사이의 거리를 계산하는 함수
def distance_(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# 사각형의 중심, 너비, 높이, 각도가 주어진 경우, 사각형의 점들을 반환하는 함수
def centerrectangle_to_dots(rect):
    centerx, centery, width, height, angle = rect

    half_width = width / 2.0
    half_height = height / 2.0
    
    points = [
        (-half_width, -half_height),
        (half_width, -half_height),
        (half_width, half_height),
        (-half_width, half_height),
        (-half_width, -half_height)  # 루프를 닫기 위해 마지막 점을 다시 추가
    ]

    # 점들을 회전시키고 평행 이동
    rotated_points = []
    for x, y in points:
        # 회전
        xr = x * math.cos(angle) - y * math.sin(angle)
        yr = x * math.sin(angle) + y * math.cos(angle)
        # 평행 이동
        xt = xr + centerx
        yt = yr + centery
        rotated_points.append((xt, yt))

    return rotated_points[:-1]

# 새로 추가된 함수: 주어진 점이 사각형 내부에 있는지 확인하는 함수
def point_inside_rect(rect, dot): 
    r_dots = centerrectangle_to_dots(rect) 
    # 점이 사각형 내부에 있는지 확인

    l_ = len(r_dots)
    s_sum = 0
    for i in range(l_): 
        d_ = distance_between_point_and_segment(dot, r_dots[i % l_], r_dots[(i + 1) % l_])
        s = 0.5 * d_ * distance_(r_dots[i % l_], r_dots[(i + 1) % l_])
        s_sum += s
    cx, cy, w, h, angle = rect

    if (s_sum - w * h) / (w * h) <= 0.00001: 
        return True
    return False

# 새로 추가된 함수: 사각형과 주어진 점 사이의 최대 거리를 계산하는 함수
def max_distance_btw_rect_dot(rect, dot): 
    # 최대 거리는 항상 꼭지점에서 발생

    r_dots = centerrectangle_to_dots(rect) 

    max_d = 0
    max_dot = (-1, -1)

    for r_dot in r_dots: 
        if max_d <= distance_(r_dot, dot):
            max_d = distance_(r_dot, dot)
            max_dot = r_dot

    # 점이 사각형 내부에 있는 경우, 최대 거리는 0
    if point_inside_rect(rect, dot): 
        max_d = 0

    cx, cy, w, h, angle = rect
    if max_d < distance_(dot, [cx, cy]) + w / 2:
        print("오류 발생")
        exit()
        return "오류"
    
    return max_d, max_dot

# 새로 추가된 함수: 사각형과 주어진 점 사이의 최소 거리를 계산하는 함수
def min_distance_btw_rect_dot(rect, dot): 
    # 최소 거리는 각 선분에 대해 계산

    r_dots = centerrectangle_to_dots(rect) 

    l_ = len(r_dots)
    min_d = 10000000
    for i in range(l_): 
        d_ = distance_between_point_and_segment(dot, r_dots[i % l_], r_dots[(i + 1) % l_])
        min_d = min(d_, min_d)

    if point_inside_rect(rect, dot): 
        min_d = 0

    return min_d
