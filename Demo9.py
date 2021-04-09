# 题目：暂停一秒输出。

# 程序分析：使用 time 模块的 sleep() 函数。

import time

data = {}

for i in range(1,10):
    for j in range(1,10):
        data[str(i)]=j

for i in data:
    time.sleep(1)
    print("取出数据 ",i,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))





