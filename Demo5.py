inputArr=[]


count=int(input("输入循环次数 \n"))

for i in range(count):
    inputArr.append(int(input("输入第 {} 个数 \n".format(i+1))))

inputArr.sort()
print("输出排序结果: 正 ",inputArr)
inputArr.reverse()
print("输出排序结果: 反  ",inputArr)