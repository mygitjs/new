# len()函数。这个函数可以返回一个字符串中的字符数，即字符串的长度。下面是一个简单的示例（如果想要正确计算中英文混合字符串的长度，可以先将字符串转换为Unicode编码，再计算长度）
my_string = "Hello, World!"
string_length = len(my_string)
print("The length of the string is:", string_length)
#结果：The length of the string is: 13

chinese_string = "你好，世界！"
unicode_chinese_string = chinese_string.encode('unicode_escape').decode()
chinese_string_length = len(unicode_chinese_string)
print("The length of the Chinese string is:", chinese_string_length)


#忽略空格计算字符串长度
# 忽略字符串中的空格，只计算非空格字符的长度。这个可以通过去除字符串中的空格后再计算长度来实现，例如：
my_string = " Hello, World! "
no_space_string = my_string.replace(" ", "")
no_space_string_length = len(no_space_string)
print("The length of the string without spaces is:", no_space_string_length)
#=========

