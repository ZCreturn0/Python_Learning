#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

# im = Image.open('./images/temp.jpg')
# w,h = im.size
# im.thumbnail((w//2,h//2))
# im.save('./images/b.jpg')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('./images/blur.jpg','jpeg')

#生成验证码

#随机大写字母
def randomCapitalLetter():
    return random.randint(65,90)

#随机颜色1
def randomColor():
    return (random.randint(50,140),random.randint(60,200),random.randint(100,250))

#随机颜色2
def randomColor2():
    return (random.randint(0,255),random.randint(20,70),random.randint(100,200))

tubeWidth = 60
tubeHeight = 60
im = Image.new('RGB',(tubeWidth*4,tubeHeight),(255,255,255))
font = ImageFont.truetype('arial.ttf',36)
draw = ImageDraw.Draw(im)
for i in range(tubeWidth*4):
    for j in range(tubeHeight):
        #每个像素随机填充颜色
        draw.point((i,j),fill=randomColor())

#填充字母
for i in range(4):
    draw.text((i*tubeWidth+10,10),chr(randomCapitalLetter()),fill=randomColor2(),font=font)

image = im.filter(ImageFilter.BLUR)
image.save('./images/code.jpg','jpeg')