from app import db

class Conference(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    intro_content = db.Column(db.String)
    
    logistics_content = db.Column(db.String)
    
    title = db.Column(db.String)
    
    created_time = db.Column(db.Date)
    
    updated_time = db.Column(db.Date)
    
    view_count = db.Column(db.Integer)
    
    is_draft = db.Column(db.Boolean)
    

    def to_dict(self):
        return dict(
            intro_content = self.intro_content,
            logistics_content = self.logistics_content,
            title = self.title,
            created_time = self.created_time.isoformat(),
            updated_time = self.updated_time.isoformat(),
            view_count = self.view_count,
            is_draft = self.is_draft,
            id = self.id
        )

    def __repr__(self):
        return '<Conference %r>' % (self.id)
