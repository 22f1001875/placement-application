from config import db
from .basemodel import BaseModel

class PlacementDrive(BaseModel):
    company_id = db.Column(db.Integer, db.ForeignKey("company_profile.id"))
    job_title = db.Column(db.String(150))
    min_cgpa = db.Column(db.Float)
    opening_date = db.Column(db.Date)
    closing_date = db.Column(db.Date)
    status = db.Column(db.String(20), default="upcoming")