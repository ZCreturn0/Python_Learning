#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):
#     def start_element(self,name,attrs):
#         print("start:%s    attr:%s" % (name,attrs))

#     def char_data(self,text):
#         print("chardata:%s" % (text))

#     def end_element(self,name):
#         print("end:%s" % (name))

# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''

# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.CharacterDataHandler = handler.char_data
# parser.EndElementHandler = handler.end_element
# parser.Parse(xml)

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    #<div>
    def handle_starttag(self,tag,attrs):
        print("<%s>-----attrs:%s" % (tag,attrs))
    
    #</div>
    def handle_endtag(self,tag):
        print("<%s/>" % (tag))

    #<image/>
    def start_endtag(self,tag,attrs):
        print("tag:<%s>    attrs:%s" % (tag,attrs))

    #<..>   xxxxxxxxxxx   <..>
    def handle_data(self,data):
        print("data:%s" % (data))

    #<!-- -->
    def handle_comment(self,text):
        print("comment:%s" % (text))

html = r'''<div class="aaa"><img src="./aa/bb.jpg"/><span>密码:</span><input type="password"/></div>'''
parse = MyHTMLParser()
parse.feed(html)