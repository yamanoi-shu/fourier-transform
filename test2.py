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

fk = np.fft.fft(y)
freq = np.fft.fftfreq(N)

theory = [exp(-(2*pi*k)**2*s**2/2.0) for k in freq]
fig, ax = plt.subplots()

ax.scatter(freq, np.abs(fk), s=1, c="red") # DFTの結果
ax.scatter(freq, theory, s=1, c="blue") # 理論曲線
plt.xlim([-0.1,0.1])
plt.show()
