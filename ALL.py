import numpy as np
A = np.array([1, 2, 3, 4, 5])
print(A)


str1 = 'Hello'
str2 = "World"
print(str1 + ' ' + str2)

x = 5
if x > 0:
    print('Positive')
elif x < 0:
    print('Negative')
else:
    print('Zero')

for i in range(1, 6):
    print(i)

i = 1
while i <= 5:
    print(i)
    i += 1

def my_function(x):
    return x * 2
output = my_function(3)
print(output)


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

def extract_numbers(s):
    result = ''
    for char in s:
        if char.isdigit():
            result += char
    return result

s = 'abc123def456ghi'
numbers = extract_numbers(s)
print(numbers)

