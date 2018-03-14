# -*- encoding: utf-8 -*-
# @Time    : 2018-03-07 22:15
# @Author  : mike.liu
# @File    : elif.py

name = input('请输入你的姓名:')
age = int(input('请输入你的年龄:'))
if name == 'Alice':
    print('Hi Alice')
    print('age:',age)
elif age < 12:
    print(' You are not Alice, kiddo.')
else:
    print(' Unlike you, Alice is not an undead, immortal vampire.')




