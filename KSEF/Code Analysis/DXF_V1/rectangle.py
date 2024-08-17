import numpy as np
import ezdxf
import math
import matplotlib.pyplot as plt

from ezdxf import recover
from ezdxf.addons.drawing import matplotlib
import numpy as np
def rotate_point(x, y, angle): # 주어진 점 (x, y)를 특정 각도만큼 회전시키는 함수
    x_new = x * np.cos(angle) - y * np.sin(angle)
    y_new = x * np.sin(angle) + y * np.cos(angle)
    return x_new, y_new

# 사각형의 중심, 너비, 높이, 회전 각도를 받아서 네 꼭지점 좌표를 반환하는 함수
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

# 주어진 축(axis)과 다각형(polygon)을 받아서 해당 축에 대한 투영 범위를 반환하는 함수
def project_polygon(axis, polygon):
    dots = np.dot(axis, polygon.T)
    return [np.min(dots), np.max(dots)]

# 두 투영 범위가 겹치는지 확인하는 함수
def axis_overlap(a_min, a_max, b_min, b_max):
    return a_min <= b_max and b_min <= a_max

# 두 사각형이 교차하는지 여부를 판단하는 함수 (Separating Axis Theorem 적용)
def rectangles_intersect(rect1, rect2):
    corners1 = get_corners(rect1)
    corners2 = get_corners(rect2)
    
    # 두 사각형의 가장자리와 수직인 축을 구함
    axes1 = corners1 - np.roll(corners1, 1, axis=0)
    axes2 = corners2 - np.roll(corners2, 1, axis=0)
    axes = np.vstack([axes1, axes2])
    
    axes = axes / np.linalg.norm(axes, axis=1)[:, None]  # 축을 정규화
    
    # 각 축에 대해 투영된 범위를 비교하여 교차 여부를 확인
    for axis in axes:
        p1 = project_polygon(axis, corners1)
        p2 = project_polygon(axis, corners2)
        
        if not axis_overlap(p1[0], p1[1], p2[0], p2[1]):
            return False  # 어느 한 축에서라도 투영이 겹치지 않으면 교차하지 않음
    
    return True

# 점 P와 선분 AB 사이의 최소 거리를 계산하는 함수
def distance_between_point_and_segment(P, A, B):
    AP = P - A
    AB = B - A
    t = np.dot(AP, AB) / np.dot(AB, AB)
    if 0 <= t <= 1:
        C = A + t * AB
        return np.linalg.norm(P - C)
    else:
        return min(np.linalg.norm(P - A), np.linalg.norm(P - B))

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
def distance (point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# 중심, 너비, 높이, 각도가 주어진 사각형을 구성하는 점들의 좌표를 반환하는 함수
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

    return rotated_points[:-1]  # 마지막 점을 제외한 점 목록 반환
