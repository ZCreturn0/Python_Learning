#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

#get请求
# r = requests.get('https://github.com/ZCreturn0')
# print(r.text)

#get传参
# r = requests.get('https://www.douban.com/search',params={'q':'python','cat':'101'})
# print(r.url)
# print(r.encoding)
# #无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
# print(r.content)

# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

# #get设置头部
# r = requests.get('https://www.douban.com/',headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'})
# print(r.text)

# #post传参
# r = requests.post('https://accounts.douban.com/login',data={'form_email': 'aaa', 'form_password': '123456'})
# print(r.text)

# #post传json
# params = {'aa':'11','bb':'22'}
# r = requests.post('https://accounts.douban.com/login',json=params)

# #上传
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
#print(r.headers)
print(r.headers['Date'])



