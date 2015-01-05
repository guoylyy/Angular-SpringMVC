from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    name = db.Column(db.String(200))
    
    url = db.Column(db.String(500))
    
    size = db.Column(db.Float)
    

    def to_dict(self):
        return dict(
            name = self.name,
            url = self.url,
            size = self.size,
            id = self.id
        )

    def __repr__(self):
        return '<Movie %r>' % (self.id)
