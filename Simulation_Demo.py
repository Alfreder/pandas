import numpy as np
import matplotlib.pyplot as plt

S0 = 0 #初始值
I = 2 #仿真次数
T = 1 #时间周期
S = np.zeros((T + 1, I)) # T+1行 I列 矩阵
#输出矩阵形状
print(S.shape)
#矩阵初始值为0
S[0] = S0

#给矩阵赋值，每列为一个企业生命周期
for t in range(1, T + 1):
    #均匀分布（-10，10） 上期 + 本期的均匀分布值
    #每行为同一周期所有企业的上期绩效 + 本期绩效
    S[t] = S[t - 1] + np.random.uniform(-10,10,I)
#输出矩阵
print(S)

#作图，按列
plt.plot(S[:, :], lw=1.5)
plt.xlabel('time')
plt.ylabel('price')
plt.show()