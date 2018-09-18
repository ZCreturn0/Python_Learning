#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
import smtplib
from email.utils import parseaddr,formataddr
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#格式化地址
def _formataddr(addr):
    header,address = parseaddr(addr)
    return formataddr((Header(header,'utf-8').encode(),addr))

#邮箱
msg_from = input('from:')
#生成的随机密码
password = input('password:')
#收取邮箱
to = input('to:')
#smtp.qq.com
smtp_server = input('server:')#'smtp.qq.com'
#QQ邮箱端口465
port = 465

# msg = MIMEText('send a msg','plain','utf-8')
# msg = MIMEText('<h2><a href="https://www.baidu.com">百度</a><h2><h5>23333333333333<h5>','html','utf-8')
msg = MIMEMultipart('alternative')
msg['From'] = _formataddr('666 %s' % msg_from)
msg['To'] = _formataddr('777 %s' % to)
msg['Subject'] = Header('嵌入图片测试','utf-8').encode()

with open('./images/a.jpg','rb') as f:
    mine = MIMEBase('image','jpg',filename='send.jpg')

    mine.add_header('Content-Disposition','attachment',filename='send.jpg')
    mine.add_header('Content-ID','<0>')
    mine.add_header('X-Attachment-Id','0')

    mine.set_payload(f.read())
    encoders.encode_base64(mine)
    msg.attach(mine)

#低版本显示
msg.attach(MIMEText('send a msg','plain','utf-8'))
#高版本显示
msg.attach(MIMEText('<html><body><h2><a href="https://www.baidu.com">百度</a><img src="cid:0"><h2><h5>嵌入图片测试aaaa<h5></body></html>','html','utf-8'))

#QQ邮箱采用https协议
server = smtplib.SMTP_SSL(smtp_server,port)
# #建立安全连接,https
# server.starttls()
server.set_debuglevel(1)
server.login(msg_from,password)
server.sendmail(msg_from,[to],msg.as_string())
server.quit()
