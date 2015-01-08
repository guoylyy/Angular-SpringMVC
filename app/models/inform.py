from app import db

class Inform(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    title = db.Column(db.String(500))
    
    create_time = db.Column(db.DateTime)
    

    def to_dict(self):
        return dict(
            title = self.title,
            create_time = self.create_time.isoformat(),
            id = self.id
        )

    def __repr__(self):
        return '<Inform %r>' % (self.id)
