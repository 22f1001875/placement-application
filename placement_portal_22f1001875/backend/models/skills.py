from config import db
from .basemodel import BaseModel

class Skill(BaseModel):
    name = db.Column(db.String(100), unique=True)