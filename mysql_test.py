#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
# 注意把password设为你的root口令:
try:
    config = {
        'user':'root',
        'password':'jiang815'
    }
    DB_NAME = 'test'
    
    
    conn = mysql.connector.connect(**config)
    conn.database = DB_NAME
    cursor = conn.cursor()#用来执行DDL语句
    # 创建user表:
    #cursor.execute('drop table user')
    #cursor.execute('create table user (id varchar(20) primary key, name varchar(20),password varchar(256))')
    cursor.execute('insert into user (id, name,password) values (%s,%s,%s)', ['1', 'Michael','jiang81533'])

    # 提交事务:
    conn.commit()
    cursor.close()
    # 运行查询:
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', ('1',))
    values = cursor.fetchall()

    # 关闭Cursor和Connection:
    cursor.close()
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    conn.close()