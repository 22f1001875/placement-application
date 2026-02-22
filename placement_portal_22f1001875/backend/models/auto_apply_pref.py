from config import db
from .basemodel import BaseModel

class AutoApplyPreference(BaseModel):
    student_id = db.Column(db.Integer, db.ForeignKey("student_profile.id"))
    enabled = db.Column(db.Boolean, default=False)