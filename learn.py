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