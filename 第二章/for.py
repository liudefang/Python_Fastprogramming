# -*- encoding: utf-8 -*-
# @Time    : 2018-03-15 22:05
# @Author  : mike.liu
# @File    : for.py
#12． 在 for 循环 中， range( 10)、 range( 0, 10) 和 range( 0, 10, 1) 之间 的 区别 是什么？
#13． 编写 一 小 段 程序， 利用 for 循环， 打 印出 从 1 到 10 的 数字。 然后 利用 while 循环， 编写 一个 等价 的 程序， 打 印出 从 1 到 10 的 数字。

for i in range(10):
    print(i)

for y in range(0,10):
    print(y)

for x in range(0,10,1):
    print(x)

for m in range(1,11):
    print(m)

n = 1
while n < 11:
    print(n)
    n=n+1