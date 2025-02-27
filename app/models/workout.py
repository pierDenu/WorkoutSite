from app import db
from app.models.basemodel import BaseModel


class Workout(BaseModel):
    __tablename__ = 'workout'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    # Many-to-many relationship with Exercise
    exercises = db.relationship('Exercise', secondary='workout_exercise', back_populates='workouts')
    plans = db.relationship('PlanWorkout', back_populates='workout')

    def __repr__(self):
        return f"<Workout {self.name}>"

    @classmethod
    def search_by_name(cls, name):
        return cls.query.filter(cls.name.like(f"{name}%")).all()
