"""1. 四舍五入"""

print(round(1.234, 1))
print(round(1, 1)) #输出1
print(round(1.35, 1)) #输出1.4,当值在两个边界中间时，round函数返回离他最近的偶数
print(round(135, -1)) #输出140


"""2. 格式化输出"""
print(format(1.23234, '0.2f'))
x = 123
# print(bin(x))
# print(oct(x))
# print(hex(x))

import math
print(math.sqrt(5))

"""随机函数"""

import random
s = [1,2,3,4,5,6]
print(random.choice(s))
# 提取N个不同的样本
print(random.sample(s,3))

# 打乱顺序
print(random.shuffle(s))
print(s)

#生成0-1的数
print(random.random())

# 生成随机整数
print(random.randint(1,20))



"""datatime"""
from datetime import datetime

t = '2018-02-02'
y = datetime.strptime(t,'%Y-%m-%d')
z = datetime.now()
print(z-y)