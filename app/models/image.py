from app import db
from sqlalchemy_imageattach.entity import Image as im
from sqlalchemy_imageattach.stores.fs import HttpExposedFileSystemStore, FileSystemStore

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Date)
    updated_time = db.Column(db.Date)
    name = db.Column(db.String)
    
    def to_dict(self):
        return dict(
            created_time = self.created_time.isoformat(),
            updated_time = self.updated_time.isoformat(),
            id = self.id
        )

class ImageStore(db.Model, im):
    __tablename__ = 'image_store'
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), primary_key=True)
    image = db.relationship('Image')