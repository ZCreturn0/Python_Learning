#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

user = input('user:')
password = input('password:')
database = input('database:')

conn = mysql.connector.connect(user=user,password=password,database=database)
cursor = conn.cursor()

create_table = r'''CREATE TABLE user(id int primary key auto_increment,username varchar(15) not null)'''
insert_table = "INSERT INTO user(id,username) values(%s,'%s'),(%s,'%s')" % (1,'aaa',2,'bbb')

print(insert_table)

cursor.execute(create_table)
cursor.execute(insert_table)

print(cursor.rowcount)
conn.commit()

select_table = 'SELECT * FROM User'
cursor.execute(select_table)
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()