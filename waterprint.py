#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os,sys
from PIL import Image,ImageFilter,ImageFont,ImageDraw

def waterprint(filename):
    try:
        im = Image.open(filename)
        w,h = im.size
        font1 = ImageFont.truetype('Arial.ttf',120)
        draw = ImageDraw.Draw(im)
        draw.text((w*4/5,h*4/5),"JJJJJ",font = font1,fill = (0,255,255))
        im.save(filename+"_120.jpg","jpeg")
    except IOError:
        print('Cannot open the file')
    
if __name__ == "__main__":
    waterprint("DSC01950.JPG")