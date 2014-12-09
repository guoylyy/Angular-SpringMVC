from flask import jsonify
from app import db
from app.extensions import fs_store
from app.tools import find_or_create_thumbnail
from sqlalchemy_imageattach.entity import Image, image_attachment, store_context
from sqlalchemy_imageattach.stores.fs import HttpExposedFileSystemStore, FileSystemStore
import json

news_topic = db.Table('news_topic',
    db.Column('news_id', db.Integer, db.ForeignKey('news.id')),
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'))
)

class News(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    title = db.Column(db.String)
    
    content = db.Column(db.String)
    
    create_time = db.Column(db.DateTime)
    
    update_time = db.Column(db.DateTime)
    
    author = db.Column(db.String)
    
    view_count = db.Column(db.Integer)
    
    is_draft = db.Column(db.Boolean)
    
    publisher = db.Column(db.Integer)

    icon = image_attachment('NewsImage')

    topics = db.relationship('Topic', secondary=news_topic, backref=db.backref('news_topics',
            lazy='dynamic'))

    def to_dict(self):
        with store_context(fs_store):
            return dict(
                title = self.title,
                content = self.content,
                create_time = self.create_time.isoformat(),
                update_time = self.update_time.isoformat(),
                author = self.author,
                view_count = self.view_count,
                is_draft = self.is_draft,
                publisher = self.publisher,
                id = self.id,
                icon=self.icon.locate()
            )

    def to_list_dict(self):
        with store_context(fs_store):
            return dict(
                id=self.id,
                title=self.title,
                create_time = self.create_time.isoformat(),
                author=self.author,
                publisher=self.publisher,
                icon=find_or_create_thumbnail(self,self.icon,100).locate()
                )

    def __repr__(self):
        return '<News %r>' % (self.id)


class Topic(db.Model):
    __tablename__ = 'topic'

    id = db.Column(db.Integer, primary_key = True)
    
    title = db.Column(db.String)

    images = db.relationship('TopicImage',backref='topic',lazy='dynamic')

    newss = db.relationship('News', secondary=news_topic, backref=db.backref('topic_newss',lazy='dynamic'))

    def to_dict(self):
        return dict(
            title = self.title,
            id = self.id,
            images = self.get_list_image()
        )

    def list(self):
        return dict(
                title = self.title,
                id = self.id,
                images = self.get_images_json(),
                newses = self.get_newses_json()
            )

    def get_list_image(self):
        if self.images[0]:
            return self.images[0].to_list_image()
        else:
            return None

    def get_newses_json(self):
        return [news.to_list_dict() for news in self.newss]

    def get_images_json(self):
        return [image.to_dict() for image in self.images]

class TopicImage(db.Model):
    __tablename__ = 'topic_image'
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    image = image_attachment('TopicImageStore')

    def to_dict(self):
        with store_context(fs_store):
            return dict(
                    id=self.id,
                    image_path=self.image.locate()
                )
    def to_list_image(self):
        with store_context(fs_store):
            return find_or_create_thumbnail(self, self.image,100).locate()

class TopicImageStore(db.Model, Image):
    __tablename__ = 'topic_image_store'
    topic_image_id = db.Column(db.Integer, db.ForeignKey('topic_image.id'), primary_key=True)
    topic_image = db.relationship('TopicImage')


class NewsImage(db.Model, Image):
    __tablename__ = 'news_image'
    news_image_id = db.Column(db.Integer, db.ForeignKey('news.id'), primary_key=True)
    news_image = db.relationship('News')

class NewsFile(db.Model):
    __tablename__ = "news_file"
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    filepath = db.Column(db.String)

    def to_dict(self):
        return dict(
                id=self.id,
                filename=self.filename,
                filepath=self.filepath
            )
