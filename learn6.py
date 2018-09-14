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

# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):
#     #<div>
#     def handle_starttag(self,tag,attrs):
#         print("handle_starttag--><%s>-----attrs:%s" % (tag,attrs))
    
#     #</div>
#     def handle_endtag(self,tag):
#         print("handle_endtag--><%s/>" % (tag))

#     #<image/>
#     def start_endtag(self,tag,attrs):
#         print("start_endtag-->tag:<%s>    attrs:%s" % (tag,attrs))

#     #<..>   xxxxxxxxxxx   <..>
#     def handle_data(self,data):
#         print("handle_data-->data:%s" % (data))

#     #<!-- -->
#     def handle_comment(self,text):
#         print("handle_comment-->comment:%s" % (text))

# html = r'''<div class="aaa"><img src="./aa/bb.jpg"/><span>密码:</span><input type="password"/></div>'''
# parse = MyHTMLParser()
# parse.feed(html)

from pyquery import PyQuery as pq
from urllib import request

#会议对象
class Meeting(object):
    def __init__(self,year,when,where,name):
        self.year = year
        self.when = when
        self.where = where
        self.name = name

meetingList = []

html = pq(url='https://www.python.org/events/python-events/')
ul = html(".list-recent-events")
for i in range(0,ul.find("li").length):
    year = ul.find("li").eq(i).find("p time .say-no-more").text()
    when = ul.find("li").eq(i).find("p time").text()
    where = ul.find("li").eq(i).find("p .event-location").text()
    name = ul.find("li").eq(i).find(".event-title a").text()
    m = Meeting(year,when,where,name)
    meetingList.append(m)

for item in meetingList:
    print("年份:%s" % (item.year))
    print("时间:%s" % (item.when))
    print("地点:%s" % (item.where))
    print("会议名称:%s" % (item.name))
    print('\n\n')
