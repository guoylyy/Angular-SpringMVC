from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    account = db.Column(db.String)
    
    password = db.Column(db.String)
    
    name = db.Column(db.String)
    
    role = db.Column(db.String)
    
    email = db.Column(db.String)
    
    registered_time = db.Column(db.Date)
    
    is_active = db.Column(db.Boolean)
    
    phone_number = db.Column(db.String)
    
    description = db.Column(db.String)
    
    lastlogin_time = db.Column(db.Date)
    
    myattr = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            account = self.account,
            password = self.password,
            name = self.name,
            role = self.role,
            email = self.email,
            registered_time = self.registered_time.isoformat(),
            is_active = self.is_active,
            phone_number = self.phone_number,
            description = self.description,
            lastlogin_time = self.lastlogin_time.isoformat(),
            myattr = self.myattr,
            id = self.id
        )

    def __repr__(self):
        return '<User %r>' % (self.id)
