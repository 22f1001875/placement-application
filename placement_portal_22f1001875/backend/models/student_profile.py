from config import db
from .basemodel import BaseModel

class StudentProfile(BaseModel):
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    full_name = db.Column(db.String(150))
    branch = db.Column(db.String(100))
    cgpa = db.Column(db.Float)
    graduation_year = db.Column(db.Integer)
    github_link = db.Column(db.String)