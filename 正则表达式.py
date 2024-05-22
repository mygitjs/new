import re
s = "sdfsfs234sdf55555sgj0"
numbers = re.findall(r"\d+",s) #正则表达式'\d+'表示匹配一个或多个数字，通过re.findall()方法可以将所有匹配的数字提取出来并返回一个列表。然后我们再使用join()方法将列表转化为一个字符串。
result = "".join(numbers)
print(result)
# 除了正则表达式外，我们还可以使用Python内置的filter()函数来过滤出数字字符。下面是一个示例代码
s1 = "dff3334dfasfsf67af1g"
numbers = ''.join(filter(str.isdigit,s1))
print(numbers)