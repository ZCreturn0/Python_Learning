#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print("start:%s    attr:%s" % (name,attrs))

    def char_data(self,text):
        print("chardata:%s" % (text))

    def end_element(self,name):
        print("end:%s" % (name))

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.CharacterDataHandler = handler.char_data
parser.EndElementHandler = handler.end_element
parser.Parse(xml)