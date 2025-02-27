from app import db
from app.models.basemodel import BaseModel


class Plan(BaseModel):
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    workouts = db.relationship('PlanWorkout', back_populates='plan')

    def get_workouts_by_day(self, day):
        return [
            pw.workout for pw in sorted(self.workouts, key=lambda pw: pw.order) if pw.day == day
        ]



