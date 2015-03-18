#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import time as stime
from app import db
from app.tools import find_or_create_thumbnail
from datetime import datetime, timedelta, time , date
from app.extensions import fs_store
from sqlalchemy_imageattach.entity import Image, image_attachment, store_context
from sqlalchemy_imageattach.stores.fs import HttpExposedFileSystemStore, FileSystemStore

HEADER_SIZE_LARGE = 480
HEADER_SIZE_SMALL = 150

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    account = db.Column(db.String(100))
    
    password = db.Column(db.String(200))
    
    name = db.Column(db.String(100))

    nickname=db.Column(db.String(100))
    
    role = db.Column(db.String(20))
    
    email = db.Column(db.String(100))
    
    registered_time = db.Column(db.Date)
    
    is_active = db.Column(db.Boolean)
    
    phone_number = db.Column(db.String(50))
    
    description = db.Column(db.Text)
    
    lastlogin_time = db.Column(db.Date)
    
    myattr = db.Column(db.String(200))
    
    token = db.Column(db.String(500))

    is_vip = db.Column(db.Boolean)

    company = db.Column(db.String(100))

    header_icon = image_attachment('UserHeader')

    department = db.Column(db.String(100))

    title = db.Column(db.String(100))

    work_phone = db.Column(db.String(100))

    zone = db.Column(db.String(100))

    def to_dict(self):
        with store_context(fs_store):
            return dict(
                account = self.account,
                name = self.name,
                role = self.role,
                email = self.email,
                password = self.password,
                nickname=self.nickname,
                registered_time = self.registered_time.isoformat(),
                is_active = self.is_active,
                phone_number = self.phone_number,
                description = self.description,
                lastlogin_time = self.lastlogin_time.isoformat(),
                myattr = self.myattr,
                token = self.token,
                id = self.id,
                is_vip = self.is_vip,
                zone = self.zone,
                work_phone = self.work_phone,
                title = self.title,
                department = self.department,
                company = self.company,
                header_large = find_or_create_thumbnail(self, self.header_icon, HEADER_SIZE_LARGE).locate(),
                header_small = find_or_create_thumbnail(self, self.header_icon, HEADER_SIZE_SMALL).locate(),
            )
    def to_header_dict(self):
        with store_context(fs_store):
            return dict(
                name = self.name,
                nickname = self.nickname,
                is_vip = self.is_vip,
                company = self.company,
                id = self.id,
                header_small = find_or_create_thumbnail(self, self.header_icon, HEADER_SIZE_SMALL).locate(),
            )   

    def __repr__(self):
        return '<User %r>' % (self.id)

    def generate_token(self):
        """
            Genterate a new token for user
        """
        MD5_RANDOM = 'testmd5'
        EXPIRE_DATA = 10
        expire_time = (datetime.now() + timedelta(EXPIRE_DATA,0)).timetuple();
        expire_datetime = stime.mktime(expire_time)
        expire = str(int(expire_datetime))
        s = '%s:%s:%s' % (self.id, expire, MD5_RANDOM)
        md5 = hashlib.md5(s.encode('utf-8')).hexdigest()
        self.token = md5+":"+expire
        #print self.token
        return True


class UserHeader(db.Model, Image):
    __tablename__ = 'user_header'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User')
