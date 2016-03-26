#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import struct 
import hashlib

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
	
hashlib_test()