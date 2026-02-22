from config import db
from .basemodel import BaseModel

class DriveSkillRequirement(BaseModel):
    drive_id = db.Column(db.Integer, db.ForeignKey("placement_drive.id"))
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"))