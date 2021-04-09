# 题目：将一个列表的数据复制到另一个列表中。

# 程序分析：使用列表[:]。

import Demo6

array1= Demo6.fib(20)
print("原始数列",array1,len(array1))
array1.reverse()
array2=array1[:]

print("复制数列 ",array2,len(array2))


