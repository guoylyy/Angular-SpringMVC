from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    content = db.Column(db.String)
    
    created_time = db.Column(db.Date)
    
    publisher = db.Column(db.String)
    
    is_active = db.Column(db.Boolean)
    

    def to_dict(self):
        return dict(
            content = self.content,
            created_time = self.created_time.isoformat(),
            publisher = self.publisher,
            is_active = self.is_active,
            id = self.id
        )

    def __repr__(self):
        return '<Message %r>' % (self.id)
