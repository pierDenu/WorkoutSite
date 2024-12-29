from app import db
from app.models.basemodel import BaseModel


class Workout(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    # Many-to-many relationship with Exercise
    exercises = db.relationship('Exercise', secondary='workout_exercise', back_populates='workouts')
    plans = db.relationship('PlanWorkout', back_populates='workout')

    def __repr__(self):
        return f"<Workout {self.name}>"

