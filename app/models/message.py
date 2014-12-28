#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import db
from app.models.user import User
from app.tools import _mk_timestamp

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    content = db.Column(db.Text)
    
    created_time = db.Column(db.DateTime)
    
    publisher = db.Column(db.String(100))
    
    is_active = db.Column(db.Boolean, default=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User')

    def to_dict(self):
        return dict(
            content = self.content,
            created_time = _mk_timestamp(self.created_time),
            publisher = self.publisher,
            is_active = self.is_active,
            id = self.id,
            user = self.user.to_header_dict()
        )

    def __repr__(self):
        return '<Message %r>' % (self.id)

class Placard(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String)

    order = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            id = self.id,
            title = self.title,
            order = self.order
            )