# -*- encoding: utf-8 -*-
# @Time    : 2018-03-14 21:37
# @Author  : mike.liu
# @File    : swordfish.py

while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print(' Hello, Joe. What is the password? (It is a fish.)')
    passwd = input()
    if passwd == 'swordfish':
        break
    print(' Access granted.')



