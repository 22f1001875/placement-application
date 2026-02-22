from config import db
from .basemodel import BaseModel

class Application(BaseModel):
    student_id = db.Column(db.Integer, db.ForeignKey("student_profile.id"))
    drive_id = db.Column(db.Integer, db.ForeignKey("placement_drive.id"))
    status = db.Column(db.String(30), default="applied")
    source = db.Column(db.String(20), default="manual")
    __table_args__ = (
        db.UniqueConstraint("student_id", "drive_id"),
    )