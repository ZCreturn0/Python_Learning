#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import String,Integer,Column,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 基类
Base = declarative_base()

class User(Base):
    #表名
    __tablename__ = 'user'

    #表结构
    #String(..),Integer,Text,Boolean,SmallInteger,DateTime
    #index=True 表示在该列创建索引
    id = Column(Integer,primary_key=True)
    username = Column(String(15),nullable=False)

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()
user = User(id=3,username='ccc')
session.add(user)
session.commit()

#one()返回第一个对象,all()返回所有结果,返回一个list
selectUser = session.query(User).filter(User.id == 2).one()
print(selectUser)
print('id:%s,username:%s' % (selectUser.id,selectUser.username))

session.close()