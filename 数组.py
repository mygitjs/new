
import numpy as np
A = np.array([1,3,3,4,5])
print(A)
str1 = "hello"
str2 = 'world'
print(str1 + " " + str2)

x = 5
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")


for i in range(1,6):
    print(i)
for i in range(2,6):
    print(i)

def my_function(x):
    return x*2
output = my_function(2)
print(output)

# 运行以下代码，将会得到一张sin函数的图像。
import matplotlib.pyplot as plt
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
plt.plot(x,y)
plt.show()
# 运行以上代码，将会得到一张sin函数的图像。

# 使用循环遍历字符串
def a(b):
    result = ""
    for c in b:
        if c.isdigit():
            result += c
    return result
s = "asfs21dfds55sdfsf878ggd"
numbers = a(s)
print(numbers)