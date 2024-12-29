from app.models.basemodel import BaseModel
from app import db

class PlanWorkout(BaseModel):
    __tablename__ = 'plan_workout'
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    day = db.Column(db.String(9), primary_key=True)

    # Відносини
    plan = db.relationship('Plan', back_populates='workouts')
    workout = db.relationship('Workout', back_populates='plans')

    @classmethod
    def get_workout_id_by_plan_and_day(cls, plan_id, day):
        workout_id = cls.query.filter(cls.day == day,
        cls.plan_id == plan_id).first().workout_id
        return workout_id


