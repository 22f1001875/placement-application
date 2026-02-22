from config import db
from .basemodel import BaseModel

class StudentSkill(BaseModel):
    student_id = db.Column(db.Integer, db.ForeignKey("student_profile.id"))
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"))
    level = db.Column(db.String(50))