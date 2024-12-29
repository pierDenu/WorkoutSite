from app import db
from app.models.basemodel import BaseModel


class Plan(BaseModel):
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    workouts = db.relationship('PlanWorkout', back_populates='plan')



