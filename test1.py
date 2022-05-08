import numpy as np
from math import sqrt, pi, exp
import matplotlib.pyplot as plt

N = 4096 # サンプル数
s = N/256 # 標準返済

y = []

for i in range(N):
    x = i - N/2
    v = exp(-x**2/(2.0*s**2))/(sqrt(2*pi)*s)
    y.append(v)

plt.plot(y)
plt.xlim([N/2-100, N/2+100])
plt.show()
