import math
import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt


def get_b0(H):
    A = (2.5 * math.pi - 5 / 3) * H
    B = H / 3
    C = 2 * H / 15 - 0.13424
    return scipy.optimize.fsolve(lambda x: A * x ** 2 + B * x + C, 0)[0]


def ellipse_platform(a, b0, H0, t_Data):
    V_Data = []
    for t in t_Data:
        b, H = get_params(H0, b0, delta_l, t)
        V_Data.append(2.5 * math.pi * H * b ** 2 + (5 * a ** 2 + 5 * a * b - 10 * b ** 2) * H / 6)
    return V_Data


def get_params(H0, b0, delta_l, t):
    H = H0 - delta_l * t
    b = b0 - delta_l * t
    return b, H


a = 0.4
H0_data = np.linspace(0.14, 0.3, 5)
e_b = math.pi * 2.5 * a ** 2
delta_l = 0.005 * 18.7 * e_b / 3600
t_data = np.linspace(0, 10000, 10000)
H_test = H0_data[0]
b_test = get_b0(H_test)
t_max = 0

# Determine the range of t
for t in t_data:
    b, H = get_params(H_test, b_test, delta_l, t)
    if 2.5 * math.pi * H * b ** 2 + (5 * a ** 2 + 5 * a * b - 10 * b ** 2) * H / 6 <= 0:
        t_max = int(t)
        break
t_data = np.linspace(0, t_max, 10 * t_max)

# draw the function image
plt.xlabel(u'Time(s)')
plt.ylabel(u'Model volume(m³)')
for H0 in H0_data:
    b0 = get_b0(H0)
    plt.plot(t_data, ellipse_platform(a, b0, H0, t_data), label='H0 = {}, l_tx0 = {}'.format(H0, b0))
plt.legend()
plt.show()
