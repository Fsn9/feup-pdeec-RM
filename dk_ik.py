import numpy as np
from math import sin, cos

def H(theta, d, a, alpha):
  return np.array([[cos(theta), -sin(theta) * cos(alpha), sin(theta) * sin(alpha), a * cos(theta)],\
                   [sin(theta), cos(theta) * cos(alpha), -cos(theta) * sin(alpha), a * sin(theta)],\
                   [0, sin(alpha), cos(alpha), d],\
                   [0, 0, 0, 1]
                   ])

# Direct kinematics
## 1. Parameters
theta1, theta2, theta3, theta4 = 0, np.deg2rad(90), 0, 0
d1, d2, d3, d4 = 1, 0, 0, 0
a1, a2, a3, a4 = 0, 1, 1, 1
alpha1, alpha2, alpha3, alpha4 = np.deg2rad(90), 0, 0, 0

## 2. Transformation matrices
h01 = H(theta1, d1, a1, alpha1)
h12 = H(theta2, d2, a2, alpha2)
h23 = H(theta3, d3, a3, alpha3)
h34 = H(theta4, d4, a4, alpha4)

## 3. Final homogenous matrices
h04 = np.linalg.multi_dot((h01,h12,h23,h34))

print(f'Final position is {h04[:3, 3]}')

# Inverse kinematics
