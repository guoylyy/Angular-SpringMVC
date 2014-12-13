from app import db

class Conference(db.Model):
    __tablename__ = 'conference'
    id = db.Column(db.Integer, primary_key = True)
    
    intro_content = db.Column(db.Text)
    
    logistics_content = db.Column(db.Text)
    
    title = db.Column(db.String(100))
    
    created_time = db.Column(db.DateTime)
    
    updated_time = db.Column(db.DateTime)
    
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

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

ConferenceAttachmentTypeEnum = Enum(['GROUP','LAYOUT','AGENDA','REPORT','PDF'])

class ConferenceFile(db.Model):
    __tablename__ = 'conference_file'
    id = db.Column(db.Integer, primary_key=True)
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'))
    file_name = db.Column(db.String(200))
    file_path = db.Column(db.String(500))
    file_type = db.Column(db.String(50)) #this should be enum

    def to_dict(self):
        return dict(
                id=self.id,
                conference_id=self.conference_id,
                file_name=self.file_name,
                file_path=self.file_path,
                file_type=self.file_type
            )



