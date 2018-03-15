# -*- encoding: utf-8 -*-
# @Time    : 2018-03-15 21:44
# @Author  : mike.liu
# @File    : exitExample.py
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed' + response + '.')