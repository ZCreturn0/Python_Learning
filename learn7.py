#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image,ImageFilter

im = Image.open('./images/temp.jpg')
w,h = im.size
im.thumbnail((w//2,h//2))
im.save('./images/b.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('./images/blur.jpg','jpeg')