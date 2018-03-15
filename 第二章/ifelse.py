# -*- encoding: utf-8 -*-
# @Time    : 2018-03-15 21:57
# @Author  : mike.liu
# @File    : ifelse.py
#9．编写代码，如果变量spam中存放1，就打印Hello，如果变量中存放2，就打印Howdy，
# 如果 变量 中 存放 其他 值， 就 打印 Greetings!

spam = int(input('请输入你的数据:'))
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')