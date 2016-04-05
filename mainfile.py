#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#告诉python解释器按照utf-8读取源文件

import math
import re
import base64
import os,sys
import locale
import random
import socket
import struct 
import hashlib
import socket
import threading
import time
import mysql.connector
from wsgiref.simple_server import make_server
from hello import application

from datetime import datetime,timedelta,timezone#first datetime is a module 2nd is class
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter
from xml.parsers.expat import ParserCreate
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
from PIL import Image,ImageFilter,ImageFont,ImageDraw

def print_input():
    #print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)原形
    name = input("Enter your name> ")
    print("Hello ",name)
    print("Wow it is","so cool")
    print("Wow it isso cool")
    print("300+100 =",300+100)
    
def data_type_var():
    print("I\'m \"pythoner\"\nLife is short\\I use python")
    print(r"\\\t\\"*10)#带有r开头就不会进行转置
    print('''ente
    r line 
    feed''')#如果使用“”多行会报错
    print("3>5 True of false? ",3>5)
    a = 123#python中 任何数据都是对象
    print("a is",a)
    a = "ABC"#创建“ABC”，创建变量a，将a指向“ABC”
    print("a is ",a)#python 为动态类型
    b = a
    a = "DEF"#虽然给a赋了新值，但是“ABC”仍然存在，b也仍然指向“ABC”
    print("b is",b)
    PI = 3.141592 #习惯用全部大写用来表明是常量，但实际仍可以改变
    print(10/3, 10//3, 10//4)#//为地板除
    print(r'Hello, "Bart"')
    print('Hello, "Bart"')
    print(r'''Hello, lisa
     mark!''')
    print('''Hello, lisa
     mark!''')

def encode_string():
    #ASCII一个字节，包含127个字母，GB2312包含中文且兼容ASCII
    #Unicode包含2个字节，生僻字包含4个字节，包含中文、日文、韩文等，在ASCII码前面补0，计算机内存统一用这个
    #由于Unicode只包含英文时候太浪费空间，因此出了可变长度的UTF-8，英文1个字节，中文3个字节，生僻字4-6字节，保存或传输时候用这个
    #浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器
    
    print(ord('A'))
    print(ord('中'))
    print(str(66))
    print('\u4e2d\u6587')
    print("'ABC' lenth: ",len("ABC"))#在内存中，str以unicode存储，一个字符有若干的字节表示，针对str计算字符数
    print("b'ABC' lenth: ",len(b"ABC"))#如果要保存在磁盘或网络传输需要转换为byte类型，以b开头，每个字符只占用一个字节，针对byte计算字节数
    print(len("中文"))
    print(len("中文".encode("utf-8")))
    print(b"ABC")
    print("ABC".encode("ASCII"))#通过encode将unicode编码为指定类型的bytes，纯英文转换后可用ASCII表示因此两者内容一样
    print("中文".encode("utf-8"))#转换后不能用ASCII显示，因此显示为\x##
    print( b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))#从网络读取、硬盘读取的都是byte类型，要转换成str
    
    sa = 88
    sb = 98
    sw = "小明"
    print("Hello, %s 15年1月成绩为%03d,15年2月成绩为%2d,提升百分点为%3.1f%%" % (sw,sa,sb,100*(sb/sa-1)))
    
    
def list_tuple():

    list_classmate = ["JWN","JXF","FXX","YWH","嘟嘟","趴趴","咩咩","旺旺","喵喵"]
    print(list_classmate)
    print(list_classmate[0])
    print(list_classmate[2])
    print("last one：",list_classmate[-1])
    print("The -lenth one：",list_classmate[-len(list_classmate)])
    print("last one:",list_classmate[len(list_classmate)-1])
    print("The lenth before insert",len(list_classmate))
    list_classmate.append("Adam")#list是有序可变的
    print("The lenth after insert",len(list_classmate))
    list_classmate.pop()
    print("The lenth after pop",len(list_classmate))
    print("list before replace",list_classmate)
    list_classmate[0] = "蒋伟男"
    print("list after replace",list_classmate)
    list_classmate.append(123)
    list_classmate.append(True)
    list_classmate.append([555,"adfds",False])#此时计算list_classmate的长度，新加入的list也只认为是一个元素
    print("list可包含不同类型的数据",list_classmate)
    #list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
    
    #deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
    dq = deque(list_classmate)
    print('\n\n\ndeque:',dq)
    dq.append('X-man')
    print('deque:',dq)
    dq.appendleft('Superman')
    print('deque:',dq)
    
    
    L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']]
    print(L)
    print("L[1][1]:",L[1][1])
    
    tuple_classmate = (list_classmate)
    print("\n\ntuple_classmate = (list_classmate):",type(tuple_classmate))
    tuple_classmate = tuple(list_classmate)
    print("tuple_classmate = tuple(list_classmate):",type(tuple_classmate))
    print("Tuple:",tuple_classmate)
    tuple_one = (1)#默认为一个数字而不是tuple
    print("tuple_one = (1):",type(tuple_one))
    tuple_one = (1,)
    print("tuple_one = (1,):",type(tuple_one))
    tuple_change = (1,2,["A","B"])
    print("*"*10)
    print(tuple_change)
    print(tuple_change[2])
    tuple_change[2][1] = "C"#tuple不可改变，此处tuple[2]的指向并没有变，但是指向内容发生变化
    print(tuple_change)
    
    #namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
    pt = namedtuple('circle',['x','y','r'])
    p = pt(1,2,10)
    print('\n\nNamedtuple:attribute',p.x,p.y,p.r)
    print('\n\nNamedtuple:index',p[0],p[1],p[2])#tuple的特性也具有
    print('Is namedtuple instance of tuple?',isinstance(p,tuple))
    
    
def condition_test():
    zero_value = 0
    em_str = ""
    em_list = []
    if zero_value:
        print("Zero value")
    elif em_str:
        print("Empty string")
    elif em_list:
        print("Empty list")
    else:
        print("Wow!")
    
    age = input("Pls enter you age> ")
    age = int(age)
    if age >6:
        print("Teenager")
    elif age > 18:
        print("Adult")
    else:
        print("Child")
        
    L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']]
    
    for l in L:
        for ll in l:
            print(ll)
    sum = 0
    for x in list(range(10)):
        sum = sum + x
    print("sum of list(range(10))",sum)
    print(list(range(10)))
    
    t = 0
    while sum>0:
        sum = sum -2
        t = t+1
    print("T value:",t)    
    
def dic_set():
    my_dict = {"JWN":95,"FXX":78,"JXF":99,"YWH":21}#查询速度快，但是会占用大量内存，其中key必须是不可变对象，比如int str，list就不可以作为key
    dict_func=dict([("JWN",95),("FXX",78),("JXF",99),("YWH",21)])
    print("******dict*******")
    print('my_dict:',my_dict)
    print('dict_func:',dict_func)
    my_dict['Adam'] = 38
    print(my_dict)
    my_dict['Adam'] = 88#一个key只能对应一个value，因此再次赋值会覆盖
    print(my_dict)#存入无序，因此每次打印结果会不一样
    print(my_dict['JWN'])
    print(my_dict.get('JWN'))
    #print(my_dict['JWK']) 如果key不存在会直接报错
    print(my_dict.get('JWK'))
    print(my_dict.get('JWK',-1))
    print("Pop action:",my_dict.pop('Adam'))#返回删除的值
    
    #普通dict，当调用的key不存在时候会报错，因此dd为了解决这个问题，不存在时候返回默认值
    #不存在key时可以返回默认值，默认值是通过函数调用返回的，函数在生成defaultdict时候定义的
    
    dd = defaultdict(lambda:'N/A')
    dd['123'] = 123
    print('******Default dict*****')
    print('dd[123]:',dd['123'],"dd['222']",dd['222'])
    
    od = OrderedDict([("JWN",95),("FXX",78),("JXF",99),("YWH",21)])#有序的dict按照插入顺序排序
    print('\n\n******Ordered dict*******')
    print(od)
    
    print('\n\n*********Set*********')
    my_set = set(list(range(5)))#只存储key不存value
    print(my_set)
    my_set = set([1,2,4,5,6,2,2,1])#存储的key不重复
    print(my_set)
    my_set.add(4)
    print("After add 4",my_set)
    my_set.add(14)
    print("After add 14",my_set)
    my_set.remove(4)
    print("After remove 4",my_set)
    
    tuple_ex = (1,2,3)
    print("set((1,2,3))",set(tuple_ex))
    my_set.add(tuple_ex)
    print("set add tuple",my_set)
    my_dict[123] = tuple_ex
    print("my_dict add tuple as value",my_dict)
    
    
    print("*"*10,"set part","*"*10)
    s1 = {1,2,3,4}
    s2 = {3,4,5,6}
    #set为无序、不重复的集合，因此可以做集合运算
    print("s1:",s1,"\ns2:",s2,"\ns1&s2:",s1&s2,"\ns1|s2",s1|s2)
    
    a = "abc"
    print("a before replace",a)
    b = a.replace('a','A')#replace创造了一个新的str 因此a没有变化，str是不可变对象
    print("a after repalce",a)
    a = ['b','c','a']#list是可变对象，对list操作是会影响list内部
    print("a before sort",a)
    a.sort()
    print("a after sort",a)
    
    tup = (1,2,3,4,4,5)
    se = set(tup)
    print(tup[1])
    print(tup)
    print(se)
    se = set("STRING")
    print(se)
    tup = tuple("STRING")
    print(tup)
    
    print('*******Counter********')
    c = Counter()
    for ch in 'Python programming'.lower():
        c[ch] = c[ch]+1
    print(c)
    
    

def func_test():
    def my_abs(x):
        if not isinstance(x,(int,float)):
            raise TypeError("wrong input")
        if x >0:
            return x
        else:
            return -x
            
    def move(x,y,step,angle= 0):
        nx = x + step*math.cos(angle)
        ny = y + step*math.sin(angle)
        return nx,ny
        
    x,y = move(100,100,60,math.pi/6)
    print("x=%06.2f,y=%.2f" % (x,y))
    #print(my_abs("dd"))
    
def func_def():
    def return_none():
        return 
    def empty_func():
        pass
        
    print(return_none())
    print(empty_func())
        
def func_para():
    def power(x , n=2):#设置n的默认值为2,默认参数在后，必须参数在前
        s = 1
        while n>0:
            n =  n-1
            s = s*x
        return s
    print("默认参数1")
    print("power(3):",power(3))
    print("power(3,3):",power(3,3))
    
    def enroll(name,age,city="BEIJING",state="CN"):#默认参数必须指定为不可变对象，不能指定[]有坑
        print("name:",name)
        print("age:",age)
        print("city:",city)
        print("state:",state)
    print("\n\n默认参数2")
    enroll("JWN",28)
    enroll("JWN",28,"USA")#默认按照参数顺序传入
    enroll("JWN",28,state="USA")#可传入指定参数
    
    #定义可变参数，在参数名前面加上*
    def cal(*nums):
        s = 0
        print(type(nums))#可变参数实际被组成了一个tuple
        for no in nums:
            s = s + no
        print("Sum is",s)
        
    def cal_list(nums):
        s = 0
        print(type(nums))
        for no in nums:
            s = s + no
        print("Sum is",s)
        
    cal(1,2,3,4,5)
    rr =list(range(0,6))
    cal_list(rr)
    cal(*rr)#如果是一个list或tuple需要传入可变参数的函数，可以用此模式传入
    
    #关键字参数，数量可变，传入后组成一个dict
    def person(name,age,**kw):
        print('name:',name,"age:",age,"other",kw)
        kw['job']='engineer'
        print('name:',name,"age:",age,"other",kw)
        
    person('JWN',26,city="BEIJING",gender="Male")
    info = {'city':"BEIJING",'gender':"Male"}
    person('JWN',26,**info)
    #传入kw的是info的拷贝，对kw改动不会影响info
    print(info)
    
    #命名关键字参数，在关键字参数的基础上限定了参数名称，可以不按照位置传入参数
    def person2(name,age,*,city='Beijing',gender):
        print(name,age,city,gender)
    person2('JWN',26,gender='M')#规定的参数必须传入
    
   #参数组合
    def ff1(a,b,c=0,*args,**kw):
        print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
    def ff2(a,b,c=0,*,d,**kw):
        print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)   
    ff1(1,2)
    ff1(1,2,c=3)
    ff1(1,2,4)   
    ff1(1,2,4,4)
    ff1(1,2,4,4,d=5)
    ff2(1,2,d=4,e=5,f=6,ext=None)
    aa=(1,2,3,4,5,6)
    bb={'d':66,'kk':88,'jj':99}
    ff1(*aa,**bb)
    cc=(1,2,3)
    ff2(*cc,**bb)#bb中包含key为d的值 因此传入了kw中

def search_file(dire,*,fname='',ext=''):
    #print(dire)
    #file_list = [x for x in os.listdir(dire) if os.path.isfile(os.path.join(dire,x))]
    #print(file_list)
    for filein in [x for x in os.listdir(dire) if os.path.isfile(os.path.join(dire,x))]:
        #print('FILES IN',filein)
        if re.match(r'\w+.'+ext+'$',filein):
            print(filein)
    for direin in [x for x in os.listdir(dire) if os.path.isdir(os.path.join(dire,x))]:
        #print('DIRE in',direin)
        search_file(os.path.join(dire,direin))
    
def os_test():
    

    #posix:linux mac unix   nt:windows
    print('OS name:',os.name)

    #system information(windows dont support)
    #print('OS info:',os.uname())

    #enviroment variables
    #print('OS environ:',os.environ)
    #print('OS environ-"PATH":',os.environ.get('PATH'))

    #.means current path /abspath 绝对路径
    current_path = os.path.abspath('.')
    print("ABS path:",current_path,type(current_path))

    #创建新的目录str，join为了消除win和linux系统的不同
    new_path = os.path.join(current_path,'testdir3')
    print('NEW path:',new_path,type(new_path))
    #创建新的目录
    #os.mkdir(new_path)
    print(os.path.abspath('.'))
    #拆分路径，为最后一级的目录或文件
    print(os.path.split(new_path))
    #修改文件名或目录名
    #os.rename('testdir2','testdir3')
    #删除目录或文件
    #os.remove('testdir3')
    #罗列当前目录内容，返回一个list
    print(type(os.listdir('C:\\')),os.listdir('C:\\'))
    #只返回时目录的内容
    ll ='C:\\Users\\jiangwn815\\Documents\\work'
    print(os.path.isdir(ll))#如果输入参数的指向的路径不存在 则返回false
    print([os.path.splitext(x)[1] for x in os.listdir(ll) if os.path.isfile(os.path.join(ll,x))])#isfile() isdir() 如果不是绝对路径 会默认使用当前路径 
    print([x for x in os.listdir(ll) if os.path.isfile(os.path.join(ll,x))])
    #利用reg把文件名中的后缀名提取出来
    ext_name = [re.split(r'\.+',x)[1] for x in os.listdir(ll) if os.path.isfile(os.path.join(ll,x))]
    print('Ext list:',ext_name)
    c = Counter()
    for ext in ext_name:
        c[ext] = c[ext]+1
    print(c)
    
    
    li = input('Pls input the list>')
    print(li)
    for x in os.listdir('C:\\'):
        print('xxx',x)
    print([x for x in os.listdir(os.path.abspath(li))])
    print([x for x in os.listdir(li) if os.path.isfile(x)])
    search_file(li)
    
    
    
    
def reg():
    print('TEST1',re.match(r'^\d{3}\-\s*\d{0,6}','010-  28129'))#\s为空格tab等空白 \d为任意数字 *为任意个 {0,6}为0-6个
    m=re.match(r'^\d{3}(\-\s*\d{0,6})+','010-  28129-3434-123-2345-353')#由于str也用\转义因此加入r前缀 避免\\情况
    print(m)
    for kk in m.groups():#groups 返回一个tuple
        print("Group",kk)
    print("group(1)",m.group(1))
    print(re.match(r'^[P|p]y','python'))
    print(re.match(r'^[P|p]y$','python'))
    print('切分',re.split(r'[\s\,]+','a,b,c d e   f'))
    print('贪婪匹配',re.match(r'^(\d+?)(0*)$','1023000').groups())
    email = re.match(r'^\w+([._-]\w+)*@\w+([._-]\w+)*','5454545@sina.com.cn')
    if email:
        print('邮箱匹配',"Email matches")
    else:
        print('邮箱匹配',"Email don't match")
        
    tz = 'UTC-08:00'
    mm = re.match(r'^UTC([+-]\d{1,2}):00$',tz)
    print('tz value:',int(mm.group(1)),'Type:',type(int(mm.group(1))))

def datetime_test():
    now =datetime.now()#datetime有时区概念，默认为系统的时区
    print("Now:",now)  
    print('Type of now:',type(now))
    date_spec = datetime(2016,2,24,10,54)#通过datetime函数构建datetime时间
    date_str = datetime.strptime('2016-2-24 10:54:00','%Y-%m-%d %H:%M:%S')#通过字符串构建datetime时间 注意格式的字母大小写
    print("\nDate spec:",date_spec)
    print("Str2datetime:",date_str)
    
    #1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time
    #当前时间就是相对于epoch time的秒数=timestamp
    #timestamp 不受时区影响 全球任意时刻任意地点的timestamp都确定
    #timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
    #timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
    ts = now.timestamp()
    print("\n\nTimestamp(Now)",ts)#距离1970年1月1日的秒数,如果在1970年前则为负数
    #print('Type(timestamp)',type(ts))#float 小数点后表示毫秒
    
    ts_spec = date_spec.timestamp()#datetime转换为timestamp
    print("Timestamp(Spe)",ts_spec)
    
    ts_str = date_spec.timestamp()
    print("Timestamp(str)",ts_str)
    
    dt_spec = datetime.fromtimestamp(ts_spec)#timestamp转换为datetime
    dt_spec_utc = datetime.utcfromtimestamp(ts_spec)#转换为utc标准时的时间 本地时间减去8小时
    print("dt_spec:",dt_spec)
    print("dt_spec_utc:",dt_spec_utc)
    print('Type of dt_spec',type(dt_spec))
    
    #datetim转化为str
    print('',datetime.strftime(dt_spec,'%a,%b %d %H:%M'))
    
    #datetime加减
    print('\nNow',now,'2hr later',now+timedelta(hours=2))
    #默认时区属性tzinfo为none,datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间
    print('Time zone info:',now.tzinfo)
    print('UTC now:',datetime.utcnow())#获得UTC标准时间
    print(datetime.utcnow().tzinfo)
    
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print('DT with tz:',utc_dt)#带上了时区信息
    print(utc_dt.tzinfo)
    tz_info = timezone(timedelta(hours=8))
    print('tz delta:',tz_info,'type:',type(tz_info))
    print('dt after tz delta:',utc_dt.astimezone(tz_info))#转换到特定时区
    
    #########如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
   
def base64_test():
    #在计算机中任何数据都是按ascii码存储的，而ascii码的128～255之间的值是不可见字符。
    #而在网络上交换数据时，比如说从A地传到B地，往往要经过多个路由设备，由于不同的设备对字符的处理方式有一些不同，这样那些不可见字符就有可能被处理错误，
    #这是不利于传输的。所以就先把数据先做一个Base64编码，统统变成可见字符，这样出错的可能性就大降低了。
    
    #base64是把3个字节变成4个可打印字符
    #对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit，可表示64个可见字符
    #如果编码的二进制数据不是3的倍数，会剩下1、2个字节。Base64用\x00字节在末尾补足后，再在编码的末尾加上1、2个=号，表示补了多少字节，解码的时候，会自动去掉。
    lowerList = list(map(chr,range(97,123)))
    upperList = list(map(chr,range(65,91)))#不包含第91个
    noList = list(range(0,10))
    base64List=upperList
    base64List[0:0]=lowerList
    base64List[len(base64List):len(base64List)]=noList
    base64List.append('+')
    base64List.append('/')#构建完成有大小写字母，数字和+ /构成的64个字符
    print(base64List)
    print(base64.b64encode(b'binary\x00string'))
    print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
    
    #由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码
    #其实就是把字符+和/分别变成-和_：
    print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64decode('abcd--__'))#由于编译为4个字节，所以编译后的字符必须是4的倍数
    #Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
    #=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉
    #解码时候根据字符为4的倍数特性，再加上相应个=解码
    
    print(11 % 4,-11 % 4)#注意正负对于求模的影响
    
def xml_test():
    #操作XML有两种方法：DOM和SAX。
    #DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
    #SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
    
    #在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data
    class DefaultSaxHandler(object):
        def __init__(self):
            self.weather = {}
            
        def start_element(self,name,attrs):
            if name=='yweather:location':
                self.weather['country'] = attrs['country']
                self.weather['city'] = attrs['city']
            if name=='yweather:astronomy':
                self.weather['sunrise'] = attrs['sunrise']
                self.weather['sunset'] = attrs['sunset']
                print(self.weather)
            #print('SAX: start_element:%s, attrs:%s' % (name,str(attrs)))
            
        def end_element(self,name):
            pass#print('SAX:end_element:%s' % name)
            
        def char_data(self,text):
            if not text:
                print('SAX:char_data:%s' % text)
            
    data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
    <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
    </rss>
    '''
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(data)

def HTMLParser_Test():

    class MyHTMLParser(HTMLParser):
        def __init__(self):
            super(MyHTMLParser,self).__init__()
            self.st=False
            self.name = []
            self.loca = []
            self.tim = []
            self.state_dict={'event-title':False,'event-location':False,'event-time':False}
            
        def handle_starttag(self,tag,attrs):#attrs是个list返回若干(name，value)对，且name都被转换为小写
            if tag == 'h3' and ('class','event-title') in attrs:
                self.state_dict['event-title'] = True
            elif tag == 'span' and ('class','event-location') in attrs:
                self.state_dict['event-location'] = True
            elif tag == 'time':
                self.state_dict['event-time'] = True
            else:
                pass
        
        def handle_data(self,data):
            #去掉data为空或者都是空格的data,且当前检测到状态是event-title
            if data and not re.match('^\s*$',data):
                if self.state_dict['event-title']:               
                    self.name.append(data)#加入到event的list中
                    self.state_dict['event-title'] = False
                elif self.state_dict['event-location']: 
                    self.loca.append(data)
                    self.state_dict['event-location'] = False
                elif self.state_dict['event-time']:
                    self.tim.append(data)
                    self.state_dict['event-time'] = False
                else:
                    pass
            else:
                pass
       
        def handle_entityref(self,name):
            print('&%s;' % name)
            
        def handle_charref(self,name):
            print('&#%s;' % name)
            
        def get_output(self):
            print (locale.getdefaultlocale())#打印当前环境的编码方式
            print(self.name)
            print(self.loca)#由于网页包含了不在gbk中的字符，需要再cmd中输入chcp 65001转换为utf-8
            print(self.tim)
            
    parser = MyHTMLParser()
    html_url = 'https://www.python.org/events/python-events/'
    with request.urlopen(html_url) as url_obj:
        parser.feed(url_obj.read().decode('utf-8'))
        parser.get_output()
    
def urllib_test():
    #urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
    #urlopen接受str或者Request object
    #默认data=None如果指定data那必然是http的post请求，而且data必须是字节流，需要urlencode
    with request.urlopen('http://www.189.cn/') as f:
        #f 是http.client.HTTPResponse object
        data = f.read()
        print('geturl() fun:',f.geturl())
        print('getcode() fun:',f.getcode())
        print(type(f))
        print('Status:',f.status,f.reason)
        for k,v in f.getheaders():
            print('%s:%s' % (k,v))
        #print('data:',data.decode('utf-8'))
        
    req = request.Request('http://www.douban.com/')
    
    req.add_header('User-Agent', 
                    'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) \
                    AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as kk:
        
        print('\n\nStatus:',kk.status,kk.reason)
        print('Type:',req.type)
        print('Host:',req.host)
        print('Full url:',req.full_url)
        for k,v in kk.getheaders():
            print('%s:%s' % (k,v))
        with open('C:\\Users\\jiangwn815\\Documents\\DB\\douban.txt','w') as ddd:
            #read得到的数据是byte格式，需要解码为utf-8写到文件中去，write只能接受str
            ddd.write(kk.read().decode('utf-8'))
        #print('\n\nData:',kk.read().decode('utf-8'))
    
def rndchr():
    return chr(random.randint(65,90))
    
def rnd_color1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
    
def rnd_color2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
    
def image_test():
    input_path = os.path.abspath(input('Please input path:'))
    jpg_file = [x for x in os.listdir(input_path) 
            if os.path.isfile(os.path.join(input_path,x)) 
            and os.path.splitext(x)[1].lower()=='.jpg' #选择jpg结尾的文件
            and os.path.getsize(x)/1024 > 3000]#选择大小大于3000KB的文件
    
    
    try:
        for file_name in jpg_file:#接受系统输入
            im = Image.open(file_name)#return a Image object 否则抛出IOError
            w,h = im.size
            print('File:%s Original size:(%s %s) Mode：%s Format:%s' % (file_name,w,h,im.mode,im.format))
            
            #制作缩率图
            im.thumbnail((w/2,h/2))
            im.save(file_name+'_thumnail.jpg','jpeg')
            
            #应用模糊滤镜
            im_blur = im.filter(ImageFilter.BLUR)
            im_blur.save(file_name+'_filter.jpg','jpeg')
            
            #切长方形，image按照坐上是0，0坐标系处理，四个值分别为左，上，右，下
            box = (100,100,400,400)
            region = im.crop(box)#进行切的操作，参数为4-tuple
            region.save(file_name+'_region.jpg','jpeg')
            
            #图片的部分替换
            region = region.transpose(Image.ROTATE_180)
            im.paste(region,box)
            im.save(file_name+'_paste.jpg','jpeg')
            
            #im.show() #会调用系统的图片显示程序
    except IOError:
        print('Cannot open the file')
        
    width = 60 * 4
    height = 60 
    image1=Image.new('RGB',(width,height),(255,255,255))
    
    font1 = ImageFont.truetype('Arial.ttf',36)#字体和字号
    
    draw = ImageDraw.Draw(image1)
    
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rnd_color1())#填充背景
            
    for t in range(5):
        #填充文字
        draw.text((40*t+random.randint(35,45),10),rndchr(),font = font1,fill = rnd_color2())
    #image1 = image1.filter(ImageFilter.BLUR)    
    image1.save('code.jpg','jpeg')        


def struct_test():
    with open('./ddd.jpg','rb') as f:
        b=f.read(16)

    print(b)
    print(struct.unpack('<ccHHBBBBIH',b))
def hashlib_test():
    ll={'dd':'12fdfdf'}
    #md5 128位 32位16进制字符表示
    md1 = hashlib.md5()
    md2 = hashlib.md5()
    #update将内容附加在后面，而不是替换内容
    md1.update('123456'.encode('utf-8'))
    ll['bob']=md5.hexdigest()
    md1.update('123456'.encode('utf-8'))
    print(md5.hexdigest())
    md2.update('123456123456'.encode('utf-8'))
    print('123456123456 md5:',md5.hexdigest())
    print('dict value:',ll)

def socket_test():
    #AF_INET 指的事IPv4协议 AF_INET6为IPv6协议
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('www.189.cn',80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.189.cn\r\nConnection: close\r\n\r\n')
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    s.close()
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件:
    with open('189.html', 'wb') as f:
        f.write(html)

def server_test():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',9999))
    s.listen(5)#最大连接数
    print('Waiting')
    
    while True:
        sock,addr = s.accept()
        
        t = threading.Thread(target=tcplink,args=(sock,addr))
        t.start()
        
def tcplink(sock,addr):
    print("Accept a new connection from %s:%s...." % addr)
    sock.send(b"Welcome")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print("Connection from %s:%s closed." % addr)
#WSGI：Web Server Gateway Interface
def wsgi_test():
    httpd = make_server('', 8000, application)
    print('Serving HTTP on port 8000...')
    # 开始监听HTTP请求:
    httpd.serve_forever()

    
if __name__ == "__main__":
    #print_input()
    #data_type_var()
    #encode_string()
    #list_tuple()
    #condition_test()
    #dic_set()
    #func_test()
    #func_def()
    #func_para()
    #os_test()
    #search_file('C:\\Users\\jiangwn815\\Documents\\DB',ext='txt')
    #reg()
    #datetime_test()
    #base64_test()
    #xml_test()
    #HTMLParser_Test()
    #urllib_test()
    #image_test()
    #hashlib_test()
    #socket_test()
    #server_test()
    wsgi_test()