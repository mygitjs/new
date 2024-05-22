# in 关键字判断一个字符串是否包含特定子字符串
s = "hello python"
if "python" in s:
    print("字符串包含 python")
else:
    print("字符串不包含 python")

#=========
#find() 方法 查找特定子字符串在字符串中的位置，如果找到则说明字符串包含该子字符串，示例代码如下
s = "hello python"
if s.find("python") != -1:
    print("字符串包含 python")
else:
    print("字符串不包含 python")
#=========
# index() 方法来查找特定子字符串在字符串中的位置，如果找到则说明字符串包含该子字符串，示例代码如下
s = "hello python"
try:
    s.index("python")
    print("字符串包含 python")
except ValueError:
    print("字符串不包含 python")
#=========
# Python 是区分大小写的，因此 “python” 和 “Python” 是两个不同的子字符串。如果想忽略大小写进行判断，可以将字符串都转换为小写或大写再进行比较，示例如下
s = "hello Python"
sub_str = "python"
if sub_str.lower() in s.lower():
    print("字符串包含 python")
else:
    print("字符串不包含 python")

#使用负数索引访问倒数第二个字符
# 在Python中，可以使用负数索引来访问字符串中倒数第二个字符。通常，索引从0开始，表示第一个字符；而负数索引从-1开始，表示倒数第一个字符。因此，要获得倒数第二个字符，可以使用索引-2。下面是一个示例：
s = "hello world"
second_last_char = s[-2]
print(second_last_char)

s = "Hello"
second_last_char = s[-2]
s = "Python"
second_last_char = s[-1]

