#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import pdb
#debug，info，warning，error
logging.basicConfig(level=logging.INFO)

# def foo(num):
#     assert num != 0,'num is 0'
#     return 10 / num
# print(foo(2))
#print(foo(0))

# logging.info('---calc:---')
# logging.error(10/0)

s= '0'
n = int(s)
pdb.set_trace()
print(10/n)