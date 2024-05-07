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

# 创建一个包含6个元素的列表
my_list = [1, 2, 3, 4, 5, 6]

# 使用len()函数获取列表的长度
list_length = len(my_list)
print("列表的长度为：", list_length)

# 创建一个空列表
empty_list = []

# 使用len()函数获取空列表的长度
if len(empty_list) == 0:
    print("列表为空")
else:
    print("列表不为空")

# Pandas提供了一个方便的方法get_dummies来实现该功能。get_dummies接受一个DataFrame或者一个Series，返回一个将类别变量转换成哑变量的DataFrame。
import pandas as pd

data = {'gender': ['male', 'female', 'male', 'female'],
        'region': ['north', 'south', 'east', 'west']}
df = pd.DataFrame(data)

dummy_df = pd.get_dummies(df)
print(dummy_df)
# get_dummies函数有多个参数可以设置，下面我们列举一些常用参数：
#
# data: 需要进行哑变量处理的DataFrame或Series。
# prefix: 增加列名前缀, prefix_sep用于指定前缀的分隔符。
# drop_first: 是否删除第一个哑变量，避免多重共线性。
# dummy_na: 是否为缺失值添加哑变量列。




import numpy as np

def tangent_vector(control_points, degree, knot_vector, u):
    # Calculate the tangent vector of the B-spline curve at parameter u
    # control_points: list of control points
    # degree: degree of the B-spline curve
    # knot_vector: knot vector of the B-spline curve
    # u: parameter value

    d = np.array(control_points)
    p = degree
    U = knot_vector

    span = 0
    while span < len(U) - 1 and not (U[span] <= u < U[span+1]):
        span += 1

    N = [[0]*len(d) for i in range(p+1)]
    N[0][span] = 1
    for j in range(1, p+1):
        for i in range(span, span-j-1, -1):
            alpha = (u - U[i]) / (U[i+p+1-j] - U[i])
            N[j][i] = (1 - alpha) * N[j-1][i] + alpha * N[j-1][i+1]

    tangent = sum(N[p][i] * d[i] for i in range(len(d)))
    return tangent

def is_parallel(control_points1, degree1, knot_vector1, control_points2, degree2, knot_vector2, u):
    # Check if two B-spline curves are parallel at parameter u
    # control_points1/2: list of control points of two B-spline curves
    # degree1/2: degree of the two B-spline curves
    # knot_vector1/2: knot vectors of the two B-spline curves
    # u: parameter value to evaluate

    tangent1 = tangent_vector(control_points1, degree1, knot_vector1, u)
    tangent2 = tangent_vector(control_points2, degree2, knot_vector2, u)

    cosine_similarity = np.dot(tangent1, tangent2) / (np.linalg.norm(tangent1) * np.linalg.norm(tangent2))
    if np.isclose(cosine_similarity, 1.0, atol=1e-6):
        return True
    else:
        return False

# Example
control_points1 = [[0, 0], [1, 1], [2, 0]]
degree1 = 2
knot_vector1 = [0, 0, 0, 1, 1, 1]

control_points2 = [[0, 1], [1, 2], [2, 1]]
degree2 = 2
knot_vector2 = [0, 0, 0, 1, 1, 1]

u = 0.5
result = is_parallel(control_points1, degree1, knot_vector1, control_points2, degree2, knot_vector2, u)
print(result)  # Output: True
