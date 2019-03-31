import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scs

S0 = 0
r = 0.05
sigma = 0.25
T = 2.0
I = 5
# ST1 = S0*np.exp((r - 0.5*sigma**2)*T+sigma*np.sqrt(T)*np.random.standard_normal(I))
# plt.hist(ST1,bins = 50)
# plt.xlabel('price')
# plt.ylabel('ferquency')

M = 10
dt = T / M
S = np.zeros((M + 1, I))
S[0] = S0
print(S[0])
for t in range(1, M + 1):

    #S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * np.random.standard_normal(I))
    S[t] = S[t - 1] + np.random.uniform(-10,10,I)
    print(S[t])
plt.hist(S[-1], bins=50)
plt.xlabel('price')
plt.ylabel('frequency')
#plt.show()
plt.plot(S[:, :], lw=1.5)
plt.xlabel('time')
plt.ylabel('price')
plt.show()