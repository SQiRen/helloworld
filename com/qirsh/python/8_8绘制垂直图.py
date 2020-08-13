import numpy as np
import matplotlib.pyplot as plt

# 为在Matplotlib中显示中文，设置特殊字体
plt.rcParams['font.sans-serif'] = ['SimHei']

objects = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
y_pos = np.arange(len(objects))
performance = [10, 8, 6, 4, 2, 1]

# plt.bar(y_pos, performance, align='center', alpha=0.5)

plt.barh(y_pos, performance, align='center', alpha=0.5, color='k',
         tick_label=objects)

# plt.xticks(y_pos, objects)
# plt.ylabel('用户量')

plt.xlabel('用户量')
plt.title('数据分析程序语言使用分布情况')
plt.show()