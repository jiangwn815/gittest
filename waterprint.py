#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import sys
from PIL import Image,ImageFilter,ImageFont,ImageDraw

def waterprint(filename,text="waterprint",font_type="lhandw",font_size=120,quality=50):
    try:
        print("Opening %s......" % filename.split('\\')[-1])
        im = Image.open(filename)
        w,h = im.size
        filename = os.path.splitext(filename)[0].split('\\')[-1]
        print(filename+" size:%s x %s" % (w,h))
        
        font_type = "C:\\Windows\\Fonts\\%s.ttf" % font_type
        font1 = ImageFont.truetype(font_type,font_size)
        draw = ImageDraw.Draw(im)
        draw.text((w*7/10,h*4/5),text,font = font1,fill = (255,255,255))
        
        filename = "%s_120.jpg" % filename
        im.save(os.path.join(r'C:\Users\jiangwn815\Documents\DB\jpg_file',filename),"jpeg",quality=quality)
    except IOError:
        print('Cannot open the file')

def jpg_file_list(location):
    return 
        
def main():
    loc = r'C:\Users\jiangwn815\Pictures\Kings Canyon'
    #print(loc.split('\\')[-1])
    file_list = [os.path.join(loc,x) for x in os.listdir(loc) 
            if os.path.isfile(os.path.join(loc,x)) 
            and os.path.splitext(x)[1].lower() == '.jpg'
            ]
    for no,x in enumerate(file_list):
        print('\nProcessing %d/%d' % (no+1,len(file_list)))
        waterprint(x,text='JF@Austrulia',font_size=100,quality=80)
    else:
        print('All done')
        
if __name__ == "__main__":
    main()