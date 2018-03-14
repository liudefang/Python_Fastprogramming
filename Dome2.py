# -*- encoding: utf-8 -*-
# @Time    : 2018-01-02 21:20
# @Author  : mike.liu
# @File    : Dome2.py
import ssl
from urllib.request import Request, urlopen

context = ssl._create_stdlib_context()

#http请求
request = Request(url="https://foofish.net/pip.html",
                  method="GET",
                  headers={"Host": "foofish.net"},
                  data=None)

#Http响应
response = urlopen(request)
headers = response.info()
content = response.read() #响应体
code = response.getcode() #状态码

print("response:",response)
print("headers:",headers)
print("content:",content)
print("code:",code)