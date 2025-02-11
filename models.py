from config import db

class Skills(db.Model):
    __tablename__ = 'skills_description'  # Table name in the database

    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    competency = db.Column(db.String(15))
    years_of_experience = db.Column(db.Integer)
    date_added = db.Column(db.Date, nullable=False ,default=db.func.current_date())

    def __repr__(self):
        return f"<Skills {self.name}>"

class DeveloperAbout(db.Model):
    __tablename__ = 'developer_about'  # Table name in the database

    developer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    gmail_id = db.Column(db.String(50), nullable=False)
    linkedin_id = db.Column(db.String(50), nullable=False)
    github_id = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False)
    date_added = db.Column(db.Date, nullable=False, default=db.func.current_date())

    def __repr__(self):
        return f"<DeveloperAbout {self.name}>"