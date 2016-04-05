#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from collections import Iterable
#任何可迭代对象都可以用for in进行循环
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

for i, value in enumerate(['A', 'B', 'C']):#实现java样式的下标循环
    print(i, value)
    
#for语句调用容器的iter() iter()返回一个iter object带有__next__()函数
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

for char in "ABCDEF":
    print(char,end=" ")
    
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

class ReIter():

    def __init__(self,data):
        self.data = data
        self.index = len(data)
        self.data = self.data[::-1]
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        
        return self.data[self.index]

        
re_iter =  ReIter("cool stuff")
for ch in re_iter:
    print(ch,end=" ")

#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
#而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
#那后面绝大多数元素占用的空间都白白浪费了。
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

l = [x * x for x in range(10)]
g = (x * x for x in range(10))#保存的是算法，占用内存小
print("列表生成式",l)
print("生成器",g)
print(next(g))
print(next(g))
print(next(g))

print('sum:',sum(i for i in range(10)))

for x in g:
    print(x,end="\t")
    
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b,end="\t")
        a, b = b, a + b
        n = n + 1
    return 'done'
    
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#local variables and execution state are automatically saved between calls   
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
    
fib(6)
for i in fib_generator(6):
    print (i,end="\t")