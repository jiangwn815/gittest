#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import struct 
import hashlib
import socket

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
	#AF_INET 指的事IPv4协议
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('www.baidu.com',80))
	s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com.cn\r\nConnection: close\r\n\r\n')
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
	with open('baidu.html', 'wb') as f:
		f.write(html)

dd = []
print(dd)
socket_test()
#hashlib_test()