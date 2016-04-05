#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import asyncio
import os
from multiprocessing import Process

#unix linux mac有fork调用，父进程可以生成多个子进程
#有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务
#常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

def run_proc(name):
    print("Childe process %s(%s) start......" % (name,os.getpid()))#获取进程id

    
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 10)#子进程终止
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def pool_test():
    print('Parent process %s.' % os.getpid())
    p = Pool(9)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()#调用close()之后就不能继续添加新的Process
    p.join()#调用join()方法会等待所有子进程执行完毕
    print('All subprocesses done.')
    
    
def mulit_proc_test():
    print("Parent process %s." % os.getpid())
    #创建子进程时，只需要传入一个执行函数和函数的参数
    p1 = Process(target=run_proc,args=('test',))
    p2 = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p1.start()
    p1.join()
    p2.start()
    
    p2.join()
    print('Child process end.')
    
    
    
    
if __name__ == '__main__':
    print(379*12)
    pool_test()