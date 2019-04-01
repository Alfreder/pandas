import numpy as np
import matplotlib.pyplot as plt
'''
PyCharm 在2017.3版本之后加入了Scientific Mode，在科学计算时，可以方便的追踪变量变化等。

有时打开了scientific mode时，但文件中引入了numpy 等科学计算包时并没有被自动识别，以scientific mode运行。需要在run方法中手动设置一下。

具体步骤：
1. Settings –> Tools –> Python Scientific > Show plots in tool window 勾选
2. View 勾选 Scientific Mode
3. Run–>Edit configurations…
4. 勾选 Run with python console
'''

S0 = 0 #初始值
I = 5 #仿真次数
T = 20 #时间周期
S = np.zeros((T + 1, I)) # T+1行 I列 矩阵
#输出矩阵形状
print(S.shape)
#矩阵初始值为0
S[0] = S0

#给矩阵赋值，每列为一个企业生命周期
for t in range(1, T + 1):
    #均匀分布（-10，10） 上期 + 本期的均匀分布值
    #每行为同一周期所有企业的上期绩效 + 本期绩效
    list2 = []
    list = np.random.uniform(-10,10,I)
    #四舍五入取整数
    for i in range(0,len(list)):
        #list[i] = round(list[i])
        list2.append(round(list[i]))

    S[t] = S[t - 1] + list2
#输出矩阵
print(S)

#作图，按列
plt.plot(S[:, :], lw=1.5)
plt.xlabel('Time')
plt.ylabel('Performance')
plt.show()

