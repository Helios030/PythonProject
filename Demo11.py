# 题目：判断101-200之间有多少个素数，并输出所有素数。
#
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　　　
#  sqrt  平方根计算
# 程序源代码：
from math import sqrt

leap = 0
h = 0
for i in range(101, 200):
    k = int(sqrt(i + 1))
    for j in range(2, k + 1):
        if i % j == 0:
            leap = 0
            break

    if leap == 1:
        print('%-4d' % i)
        h += 1
        if h % 10 == 0:
          print('')
    leap = 1
print('The total is %d' % h)
