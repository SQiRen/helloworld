import numpy as np
import matplotlib.pyplot as plt

# 为在Matplotlib中显示中文，设置特殊字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 用于绘制图形的数据
n_group = 4
means_frank = [90, 55, 40, 65]
means_guido = [85, 62, 54, 20]

# 创建图形
fig, ax = plt.subplots()

# 定义条形图在横坐标上的分类位置
index = np.arange(n_group)
bar_width = 0.35
opacity = 0.8

# 绘制第一个条形图
rects1 = plt.bar(index, means_frank, bar_width, alpha=opacity,
                 color='w', edgecolor='k', hatch='......', label='张三')

# 绘制第二个条形图
# rects2 = plt.bar(index+bar_width, means_guido, bar_width, alpha=opacity,
#                  color='w', edgecolor='k', hatch='\\\\', label='李四')

# 绘制叠加条形图
rects2 = plt.bar(index, means_guido, bar_width, bottom=means_frank, alpha=opacity,
                 color='w', edgecolor='k', hatch='\\\\', label='李四')
plt.xlabel('课程')
plt.ylabel('分数')
plt.title('分数对比图')
plt.xticks(index+bar_width, ['A', 'B', 'C', 'D'])
plt.legend()
plt.show()