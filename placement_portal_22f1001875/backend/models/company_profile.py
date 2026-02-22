from config import db
from .basemodel import BaseModel

class CompanyProfile(BaseModel):
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    company_name = db.Column(db.String(200))
    approval_status = db.Column(db.String(20), default="pending")