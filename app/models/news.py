from app import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    title = db.Column(db.String)
    
    content = db.Column(db.String)
    
    create_time = db.Column(db.Date)
    
    update_time = db.Column(db.Date)
    
    author = db.Column(db.String)
    
    view_count = db.Column(db.Integer)
    
    is_draft = db.Column(db.Boolean)
    
    publisher = db.Column(db.Integer)
    

    def to_dict(self):
        return dict(
            title = self.title,
            content = self.content,
            create_time = self.create_time.isoformat(),
            update_time = self.update_time.isoformat(),
            author = self.author,
            view_count = self.view_count,
            is_draft = self.is_draft,
            publisher = self.publisher,
            id = self.id
        )

    def __repr__(self):
        return '<News %r>' % (self.id)
