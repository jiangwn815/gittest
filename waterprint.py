#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os,sys

from PIL import Image,ImageFilter,ImageFont,ImageDraw

def waterprint(filename,text="waterprint",font_type="lhandw",font_size=120):
    try:
        print("Opening "+filename+"......")
        im = Image.open(filename)
        w,h = im.size
        print(os.path.splitext(filename)[0]+" size:%s x %s" % (w,h))
        
        font_type = "C:\\Windows\\Fonts\\"+font_type+".ttf"
        font1 = ImageFont.truetype(font_type,font_size)
        draw = ImageDraw.Draw(im)
        draw.text((w*4/5,h*4/5),text,font = font1,fill = (0,255,255))
        
        im.save(filename+"_120.jpg","jpeg",quality=100)
    except IOError:
        print('Cannot open the file')
    
if __name__ == "__main__":
    waterprint("DSC01950.JPG","JF@Austrulia")