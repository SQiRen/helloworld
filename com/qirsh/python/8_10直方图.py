import numpy as np
import matplotlib.pyplot as plt

# 为在Matplotlib中显示中文，设置特殊字体
plt.rcParams['font.sans-serif'] = ['SimHei']

mu = 100     # 数学期望
sigma = 15   # 标准差
x = mu + sigma * np.random.randn(200)
num_bin = 25  # 25组
plt.figure(figsize=(9, 6), dpi=100)
n, bins, patches = plt.hist(x, num_bin, color='w', edgecolor='k',
                            hatch=r'ooo', density=1, label='频率')
y = ( ( 1/( np.sqrt( 2*np.pi )*sigma ) ) *
     np.exp( -0.5*( 1/sigma*(bins-mu ) )**2) )
print(n, bins, patches)
plt.plot(bins, y, '--', label='概率密度函数')
plt.xlabel('聪明度')
plt.ylabel('概率密度')
plt.title('IQ直方图:$\mu=100$,$\sigma=15$')

plt.legend()
plt.show()