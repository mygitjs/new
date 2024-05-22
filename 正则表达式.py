import re
s = "sdfsfs234sdf55555sgj0"
numbers = re.findall(r"\d+",s) #正则表达式'\d+'表示匹配一个或多个数字，通过re.findall()方法可以将所有匹配的数字提取出来并返回一个列表。然后我们再使用join()方法将列表转化为一个字符串。
result = "".join(numbers)
print(result)
# 除了正则表达式外，我们还可以使用Python内置的filter()函数来过滤出数字字符。下面是一个示例代码
s1 = "dff3334dfasfsf67af1g"
numbers = ''.join(filter(str.isdigit,s1))
print(numbers)
# 使用列表推导式
# 还有一种简洁的方法是使用列表推导式。我们可以通过遍历字符串，将每个数字字符保存到一个列表中，然后再将这个列表转换为字符串。下面是一个示例代码：
s = "vxcvdf3ttxtt55"
numbers = "".join([char for char in s if char.isdigit()])
print(numbers)

# 怎么获取一个数据集的所有属性 Python
import pandas as pd
data = pd.read_csv("data.csv")#加载数据集
# 获取数据集的所有属性
attributes = data.columns
print(attributes)


# 最大重试次数超过给定的url-python
import requests
# from requests.exceptions import MaxRetryError

url = "http://example.com"
max_retries = 3
for retry in range(max_retries):
    try:
        reponse = requests.get(url)
        reponse.raise_for_status()
        print("request successful")
        break
    except 0:
        print(f"Retry {retry+1}/{max_retries}")
if retry == max_retries - 1:
    print("max retries exceeded")

# 使用Retry对象实现请求重试功能
# 除了使用MaxRetryError异常外，我们还可以使用Retry对象来实现请求重试功能。Retry对象允许我们自定义重试次数、重试间隔、重试回调函数等参数，以满足不同的重试需求。
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


url = "http://example.com"
retry_strategy = Retry(
    total = 3,
    backoff_factor = 2,
    status_forcelist = [500,502,503,504]
)

adapter = HTTPAdapter(max_retries = retry_strategy)

with requests.Session() as session:
    session.mount("http://",adapter)
    session.mount("https://",adapter)
    response = session.get(url)
    response.raise_for_status()
    print("Request successful")