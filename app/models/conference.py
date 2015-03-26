from app import db

class Conference(db.Model):
    __tablename__ = 'conference'
    id = db.Column(db.Integer, primary_key = True)
    
    intro_content = db.Column(db.Text)
    
    logistics_content = db.Column(db.Text)

    group_content = db.Column(db.Text)

    layout_content = db.Column(db.Text)

    agenda_content = db.Column(db.Text)
    
    title = db.Column(db.String(100))
    
    created_time = db.Column(db.DateTime)
    
    updated_time = db.Column(db.DateTime)

    started_time = db.Column(db.DateTime)
    
    view_count = db.Column(db.Integer)
    
    is_draft = db.Column(db.Boolean) 
    
    is_show_ios = db.Column(db.Boolean) #show or not in ios device

    is_show_android = db.Column(db.Boolean) # show or not in android

    is_show_in_time = db.Column(db.Boolean) # show or not in start time

    def to_dict(self):
        return dict(
            intro_content = self.intro_content,
            logistics_content = self.logistics_content,
            group_content = self.group_content,
            layout_content = self.layout_content,
            agenda_content = self.agenda_content,
            title = self.title,
            created_time = self.created_time.isoformat(),
            updated_time = self.updated_time.isoformat(),
            started_time = self.started_time.isoformat(),
            view_count = self.view_count,
            is_draft = self.is_draft,
            is_show_ios = self.is_show_ios,
            is_show_android = self.is_show_android,
            is_show_in_time = self.is_show_in_time,
            id = self.id
        )

    def to_simple_dict(self):
        return dict(
            title = self.title,
            created_time = self.created_time.isoformat(),
            updated_time = self.updated_time.isoformat(),
            started_time = self.started_time.isoformat(),
            view_count = self.view_count,
            is_draft = self.is_draft,
            is_show_ios = self.is_show_ios,
            is_show_android = self.is_show_android,
            is_show_in_time = self.is_show_in_time,
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



