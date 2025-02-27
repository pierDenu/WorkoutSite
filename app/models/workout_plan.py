from app.models.basemodel import BaseModel
from app import db


class PlanWorkout(db.Model):
    __tablename__ = 'plan_workout'

    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), primary_key=True)
    day = db.Column(db.String(9), primary_key=True)

    order = db.Column(db.Integer, nullable=False)

    plan = db.relationship('Plan', back_populates='workouts')
    workout = db.relationship('Workout', back_populates='plans')

    @classmethod
    def get_workout_id_by_plan_and_day(cls, plan_id, day):
        return cls.query.filter(cls.day == day,
        cls.plan_id == plan_id).order_by(cls.order).all()



