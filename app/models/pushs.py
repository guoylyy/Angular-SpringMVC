from app import db

class Pushs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    content = db.Column(db.String)
    
    created_time = db.Column(db.Date)
    
    success = db.Column(db.Boolean)
    

    def to_dict(self):
        return dict(
            content = self.content,
            created_time = self.created_time.isoformat(),
            success = self.success,
            id = self.id
        )

    def __repr__(self):
        return '<Pushs %r>' % (self.id)
