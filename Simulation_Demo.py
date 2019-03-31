import numpy as np
import matplotlib.pyplot as plt


S0 = 0 #初始值
I = 20 #仿真10次
T = 10 #时间
S = np.zeros((T + 1, I))
S[0] = S0
for t in range(1, T + 1):
    #均匀分布（-10，10）
    S[t] = S[t - 1] + np.random.uniform(-10,10,I)
    #输出矩阵
    print(S[t])

plt.plot(S[:, :], lw=1.5)
plt.xlabel('time')
plt.ylabel('price')
plt.show()